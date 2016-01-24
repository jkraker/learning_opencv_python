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

# swap BGR to RGB encoding for matplotlib
b,g,r = cv2.split(img)
img = cv2.merge((r,g,b))

# code here operating on img
mod = img

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(mod),plt.title('modified')
plt.xticks([]), plt.yticks([])
plt.show()
