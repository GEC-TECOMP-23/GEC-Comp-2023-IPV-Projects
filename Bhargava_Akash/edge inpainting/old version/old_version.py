import cv2
import numpy as np
import tkinter as tk
from PIL import ImageTk, Image

drawing = False
x_start, y_start = 0, 0
x_end, y_end = 0, 0

def select_roi(event, x, y, flags, param):  #region of interest
    global x_start, y_start, x_end, y_end, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        x_start, y_start = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        x_end, y_end = x, y
        cv2.rectangle(image, (x_start, y_start), (x_end, y_end), (0, 255, 0), 2)
        cv2.imshow("Image", image)

def apply_filters():
    # Read the image
    image = cv2.imread('image.jpeg')  # Load image in grayscale
    print(image.shape)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(image, (blur_slider.get(), blur_slider.get()), 0)
    
    if threshold_mode.get() == 0:  # Local Thresholding
        
        # Define the coordinates of the ROI
        roi = image[y_start:y_end, x_start:x_end]

        # Apply thresholding to the ROI
        _, binary_roi = cv2.threshold(roi, threshold_slider.get(), 255, cv2.THRESH_BINARY)

        # Create a mask with the same dimensions as the original image
        mask = np.zeros_like(image)

        # Insert the thresholded ROI into the mask
        mask[y_start:y_end, x_start:x_end] = binary_roi
    else:  # Thresholding over the full image
        _, mask = cv2.threshold(blurred, threshold_slider.get(), 255, cv2.THRESH_BINARY)

    # Perform Canny edge detection
    edges = cv2.Canny(mask, 30, 100)

    # Dilate the edges to make them thicker
    kernel = np.ones((3, 3), np.uint8)
    dilated_edges = cv2.dilate(edges, kernel, iterations=dilation_slider.get())

    inpainted = cv2.inpaint(image, dilated_edges, inpaintRadius=3, flags=cv2.INPAINT_NS)

    # Display the result in a new window
    cv2.imshow("Inpainted Edges", inpainted)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Create the main window
root = tk.Tk()
root.title("Edge Inpainting")
root.geometry("600x400")  # Set the width and height of the window

# Create the sliders
blur_slider = tk.Scale(root, from_=1, to=31, orient=tk.HORIZONTAL, label="Blur Kernel Size")
blur_slider.set(13)
blur_slider.pack()

dilation_slider = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, label="Dilation Iter")
dilation_slider.set(5)
dilation_slider.pack()

threshold_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Threshold")
threshold_slider.set(250)
threshold_slider.pack()

# Create the threshold mode radio buttons
threshold_mode = tk.IntVar()
threshold_mode.set(0)

local_threshold_radio = tk.Radiobutton(root, text="Thresholding a Region", variable=threshold_mode, value=0)
local_threshold_radio.pack()

full_image_threshold_radio = tk.Radiobutton(root, text="Threshold over Full Image", variable=threshold_mode, value=1)
full_image_threshold_radio.pack()

# Create the apply button
apply_button = tk.Button(root, text="Apply Filters", command=apply_filters)
apply_button.pack()

# Load the image
image = cv2.imread('image.jpeg')
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", select_roi)
cv2.imshow("Image", image)

# Start the Tkinter event loop
root.mainloop()
