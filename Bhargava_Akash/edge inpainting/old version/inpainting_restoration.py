import cv2
import numpy as np
import tkinter as tk
from PIL import ImageTk, Image

def apply_filters():
    # Read the image
    image = cv2.imread('image2.jpeg')  # Load image in grayscale
    print(image.shape)

    # Apply Gaussian blur to reduce noise
    blurred = cv2.GaussianBlur(image, (blur_slider.get(), blur_slider.get()), 0)
    # _, blurred = cv2.threshold(image, 250, 255, cv2.THRESH_BINARY)

    # Define the coordinates of the ROI
    x, y, width, height = 75, 0, 160, 30

# Extract the ROI from the image
    roi = image[y:y+height, x:x+width]

# Apply thresholding to the ROI
    _, binary_roi = cv2.threshold(roi, 250, 255, cv2.THRESH_BINARY)

# Create a mask with the same dimensions as the original image
    mask = np.zeros_like(image)

# Insert the thresholded ROI into the mask
    mask[y:y+height, x:x+width] = binary_roi


    # Perform Canny edge detection with adjustable threshold values
    edges = cv2.Canny(mask, canny_min_slider.get(), canny_max_slider.get())

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
blur_slider = tk.Scale(root, from_=1, to=31, orient=tk.HORIZONTAL, label="Blur Kernel \nSize")
blur_slider.set(13)
blur_slider.pack()

canny_min_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Edge Min")
canny_min_slider.set(30)
canny_min_slider.pack()

canny_max_slider = tk.Scale(root, from_=0, to=255, orient=tk.HORIZONTAL, label="Edge Max ")
canny_max_slider.set(100)
canny_max_slider.pack()

dilation_slider = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, label="Dilation Iter")
dilation_slider.set(5)
dilation_slider.pack()

# Create the apply button
apply_button = tk.Button(root, text="Apply Filters", command=apply_filters)
apply_button.pack()

# Start the Tkinter event loop
root.mainloop()
