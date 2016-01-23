import cv2
import numpy as np

img = cv2.imread('messi5.jpg')

# 2 ways of doing the same thing:

res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)

#cv2.imwrite('messi5_x2_1.jpg', res)

#OR

height, width = img.shape[:2]
res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

#cv2.imwrite('messi5_x2_2.jpg', res)
