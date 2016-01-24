import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys

if len(sys.argv) != 3:
    print "usage:",sys.argv[0], \
        "<input file>", \
        "<integer 1-4 specifying filter type"
    print "    1: averaging"
    print "    2: Gaussian"
    print "    3: median"
    print "    4: bilateral"
    sys.exit(0)

filter_type = sys.argv[2]

img = cv2.imread(sys.argv[1])
if img == None:
    print "invalid input file",sys.argv[1]
b,g,r = cv2.split(img)
img = cv2.merge((r,g,b))

blur = None
if filter_type == '1':
    #averaging
    blur = cv2.blur(img,(5,5))
elif filter_type == '2':
    # gaussian filter
    blur = cv2.GaussianBlur(img,(5,5),0)
elif filter_type == '3':
    # median filter
    blur = cv2.medianBlur(img,5)
elif filter_type == '4':
    # bilateral filter
    blur = cv2.bilateralFilter(img,9,75,75)
else:
    print "invalid filter specified:",filter_type
    sys.exit(1)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()
