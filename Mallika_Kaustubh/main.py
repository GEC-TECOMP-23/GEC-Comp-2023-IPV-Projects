import cv2
import numpy as np
import matplotlib.pyplot as plt

refPt = []
cropping = False


def click_and_crop(event, x, y, flags, param):
    global refPt, cropping, image
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)

# Function to extract the object and save it as a mask


def extract_object(image_path, mask_path):
    global refPt, cropping, image
    image = cv2.imread(image_path)
    clone = image.copy()
    cv2.namedWindow("image", cv2.WINDOW_NORMAL)
    cv2.setMouseCallback("image", click_and_crop)

    while True:
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("r"):
            image = clone.copy()

        elif key == ord("c"):
            break

    if len(refPt) == 2:
        roi = clone[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]]
        mask = np.zeros(image.shape[:2], dtype=np.uint8)
        mask[refPt[0][1]:refPt[1][1], refPt[0][0]:refPt[1][0]] = 255
        cv2.imwrite(mask_path, mask)
    cv2.destroyAllWindows()


def erase_object(image_path, mask_path, output_path):
    image = cv2.imread(image_path)
    mask = cv2.imread(mask_path, 0)
    erased_image = image.copy()
    # Set the pixels of the object to be erased as black in the erased image
    # Set RGB channels to black
    erased_image[np.where(mask == 255)] = [0, 0, 0]

    # Apply inpainting to fill the erased region with surrounding colors
    result = cv2.inpaint(erased_image, mask, 3, cv2.INPAINT_TELEA)

    cv2.imwrite(output_path, result)

    # Display the original and erased images side by side
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    axs[0].set_title('Original Image')
    axs[0].axis('off')
    axs[1].imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    axs[1].set_title('Erased Object Image')
    axs[1].axis('off')
    plt.show()


image_path = './66.jpg'
mask_path = './mask.png'        # Path to the mask image
output_path = './erased_object.jpg'    # Path to save the erased object image


extract_object(image_path, mask_path)
erase_object(image_path, mask_path, output_path)
