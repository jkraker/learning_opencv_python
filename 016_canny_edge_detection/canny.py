import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

if len(sys.argv) != 2:
    print "usage:",sys.argv[0], \
        "<input file>"
    sys.exit(0)

img = cv2.imread(sys.argv[1])
if img == None:
    print "invalid input file",sys.argv[1]
    sys.exit(1)

# convert image to grayscale
grayscale = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img = grayscale

print img.shape

# code here operating on img
mod = cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(mod,'gray'),plt.title('modified')
plt.xticks([]), plt.yticks([])
plt.show()