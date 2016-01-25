import cv2
import numpy as np
from matplotlib import pyplot as plt
import sys
import copy

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

ret,thresh = cv2.threshold(grayscale,127,255,cv2.THRESH_BINARY)
thresholded = copy.deepcopy(thresh)
contours,hierarchy = cv2.findContours(thresh, 1, 2)

cnt = contours[0]
M = cv2.moments(cnt)
centroid = (int(M['m10']/M['m00']),int(M['m01']/M['m00']))
print 'resolution (r,c): '+str(thresholded.shape)
print 'center of mass (r,c): '+str(centroid)
cv2.circle(thresholded,centroid,10,127,-1)

print 'area: '+str(cv2.contourArea(cnt)) # or str(M['m00'])
print 'perimeter: '+str(cv2.arcLength(cnt,True))


plt.subplot(121),plt.imshow(grayscale,'gray'),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(thresholded, 'gray'),plt.title('centroid')
plt.xticks([]), plt.yticks([])
plt.show()
