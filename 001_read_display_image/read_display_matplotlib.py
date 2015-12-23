import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Dactylorhiza_majalis_Spechtensee_small.JPG')

# encoding is different (BGR) than what is expected by matplotlib (RGB)
b,g,r = cv2.split(img)
img2 = cv2.merge([r,g,b])

# plot using matplotlib
plt.imshow(img2, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([]) # hides tick values on X & Y axes
plt.show()
