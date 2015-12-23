import numpy as np
import cv2

img = cv2.imread('Dactylorhiza_majalis_Spechtensee_small.JPG',cv2.IMREAD_COLOR)
#img = cv2.imread('Dactylorhiza_majalis_Spechtensee_small.JPG') # default is color
#img = cv2.imread('Dactylorhiza_majalis_Spechtensee_small.JPG', cv2.IMREAD_GRAYSCALE) # grayscale
#img = cv2.imread('Dactylorhiza_majalis_Spechtensee_small.JPG', cv2.IMREAD_UNCHANGED) # loads as such including alpha channel

cv2.imshow('image read demo',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
