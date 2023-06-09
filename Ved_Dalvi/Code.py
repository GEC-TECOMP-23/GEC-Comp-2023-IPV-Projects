import cv2
import numpy as np
img1 = cv2.imread('original.png')

blurred =cv2.blur(img1,(5,5))
cv2.imwrite('Blurred.png',blurred)

GBlurred = cv2.GaussianBlur(img1,(5,5),0)
cv2.imwrite('GBlurred.png',GBlurred)

MBlurred=cv2.medianBlur(img1,5)
cv2.imwrite('MBlurred.png',MBlurred)


img2 = cv2.imread('blurred.png',1)
filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]) #sharpening filter

sharpen_img=cv2.filter2D(img2,-1,filter)
cv2.imwrite('sharpenedimg.png',sharpen_img)



