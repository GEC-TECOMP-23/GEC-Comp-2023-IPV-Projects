print("....Creating own filter to remove noise.....")

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('PImage4.jpg')
# plt.imshow(img)
# plt.show()
cv2.imshow('original image', img)
cv2.waitKey(0)

#...........................1 filter...................................
# Apply kernel for embossing
emboss_kernel = np.array([[-1, 0, 0],
					[0, 0, 0],
					[0, 0, 1]])

emboss_img = cv2.filter2D(src=img, ddepth=-1, kernel=emboss_kernel)

plt.imshow(emboss_img)
plt.show()

#............................2 sharpening filter...............................
# Apply kernel for sharpening
sharp_kernel = np.array([[0, -1, 0],
                    [-1, 5, -1],
                    [0, -1, 0]])
  
sharp_img = cv2.filter2D(src=img, ddepth=-1, kernel=sharp_kernel)
plt.imshow(sharp_img)
plt.show()
#..................................My own created filter ..........................................
My_filter = np.array([[1, 2, 1],
                     [-4, 0, 1],
                     [0, -2, 1]])
  
my_img = cv2.filter2D(src=img, ddepth=-1, kernel=My_filter)
plt.imshow(my_img)

plt.show()
cv2.destroyAllWindows()

