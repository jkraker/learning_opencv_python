import numpy as np
import cv2

img = cv2.imread('Dactylorhiza_majalis_Spechtensee_small.JPG', cv2.IMREAD_GRAYSCALE) # grayscale

cv2.imshow('image read demo',img)
print "press 's' to save the image as 'grayscale_flower.jpg' and ESC to exit without saving"

k = 0
while k != 27 and k != ord('s'):
   k = cv2.waitKey(0) & 0xff

if k == 27: # wait for ESC key to exit
   cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
   cv2.imwrite('grayscale_flower.jpg',img)
   cv2.destroyAllWindows()
