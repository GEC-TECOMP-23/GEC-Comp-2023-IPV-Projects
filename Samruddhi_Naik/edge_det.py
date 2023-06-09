# sobel and canny edge detection

import cv2

img = cv2.imread('C:\\Users\\HP\\OneDrive\\Desktop\\sam\\sem 6\\IPV\\pract1\\expt2\\nezuko.png',flags=0)
img = cv2.resize(img,(500,300))
cv2.imshow("original",img)
######### soble edge detection #########

img_blur = cv2.GaussianBlur(img,(3,3), 0, 0)
sobelx = cv2.Sobel(img_blur, ddepth=cv2.CV_64F,dx= 1, dy=0,ksize=3) # ddepth specifies the precision of the output image
sobely = cv2.Sobel(img_blur, ddepth=cv2.CV_64F,dx= 0,dy= 1,ksize=3)
sobelxy = cv2.Sobel(img_blur, ddepth=cv2.CV_64F,dx= 1,dy= 1,ksize=3)

cv2.imshow("sobelx",sobelx)
cv2.imshow("sobely",sobelx)
cv2.imshow("sobelxy",sobelxy)

cv2.imwrite("sobelx.png",sobelx)
cv2.imwrite("sobely.png",sobelx)
cv2.imwrite("sobelxy.png",sobelxy)

######### canny edge detection #########
canny1 = cv2.Canny(img,100,200, apertureSize=5,L2gradient = True)
canny2 = cv2.Canny(img,100,200, apertureSize=5)
canny3 = cv2.Canny(img,100,200,L2gradient = True)

cv2.imshow("canny 1 ",canny1)
cv2.imshow("canny 2 ",canny2)
cv2.imshow("canny 3 ",canny3)

cv2.imwrite("canny 1.png ",canny1)
cv2.imwrite("canny 2.png ",canny2)
cv2.imwrite("canny 3.png ",canny3)
#######################################


cv2.waitKey(0)
cv2.destroyAllWindows()