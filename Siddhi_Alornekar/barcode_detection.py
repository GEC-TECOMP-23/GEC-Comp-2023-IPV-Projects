# import the necessary packages
import numpy as np  # for Numeric processing
import imutils
import cv2

# ------------- INPUT IMAGE --------------

image_name = 'C:\\Users\\Admin\\Desktop\\Siddhi\\Programs\\IPV Project\\Project\\Img1.jpeg'
image = cv2.imread(image_name)

image = cv2.resize(image, (1000, 600)) 
cv2.imshow('Original Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------- 1. GRAYSCALE --------------

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imwrite('C:\\Users\\Admin\\Desktop\\Siddhi\\Programs\\IPV Project\\Project\\Grayscale.jpeg', gray)
cv2.imshow('Gray Scale', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------- 2. GRADIENT --------------

# Compute the Scharr gradient magnitude representation of the images
# In both the x and y direction 

ddepth = cv2.cv.CV_32F if imutils.is_cv2() else cv2.CV_32F
gradX = cv2.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=-1)
gradY = cv2.Sobel(gray, ddepth=ddepth, dx=0, dy=1, ksize=-1)

# Subtract the y-gradient from the x-gradient
gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)

cv2.imwrite('C:\\Users\\Admin\\Desktop\\Siddhi\\Programs\\IPV Project\\Project\\Gradient.jpeg', gradient)
cv2.imshow('Gradient',gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------- 3. BLUR IMAGE --------------

# Blur the image
blurred = cv2.blur(gradient, (9, 9))

cv2.imwrite('C:\\Users\\Admin\\Desktop\\Siddhi\\Programs\\IPV Project\\Project\\Blurred.jpeg', blurred)
cv2.imshow('Blurred',blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------- 4. BINARY THRESHOLD --------------

# Threshold the image

(_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

cv2.imwrite('C:\\Users\\Admin\\Desktop\\Siddhi\\Programs\\IPV Project\\Project\\Threshold.jpeg', thresh)
cv2.imshow('Threshold',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------- 5. MORPHOLOGY --------------

# Construct a closing kernel and apply it to the thresholded image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
morphed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

cv2.imwrite('C:\\Users\\Admin\\Desktop\\Siddhi\\Programs\\IPV Project\\Project\\Morphed.jpeg', morphed)
cv2.imshow('Morphed',morphed)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------- 6. EROSION AND DILATION --------------

# Perform a series of erosions and dilations
eroded = cv2.erode(morphed, None, iterations = 4)
eroded_and_dilated = cv2.dilate(eroded, None, iterations = 4)

cv2.imwrite('C:\\Users\\Admin\\Desktop\\Siddhi\\Programs\\IPV Project\\Project\\Eroded_Dilated.jpeg', eroded_and_dilated)
cv2.imshow('Eroded and Dilated',eroded_and_dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------- 7. FINDING CONTOURS --------------

# Find the contours in the thresholded image 
# Then sort the contours by their area
# Keep only the largest one

contours = cv2.findContours(eroded_and_dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
c = sorted(contours, key = cv2.contourArea, reverse = True)[0]

# Compute the rotated bounding box of the largest contour
rect = cv2.minAreaRect(c)
box = cv2.cv.BoxPoints(rect) if imutils.is_cv2() else cv2.boxPoints(rect)
box = np.int0(box)

# Draw a bounding box around the detected barcode and display the image
cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
cv2.imshow("Image", image)
cv2.waitKey(0)