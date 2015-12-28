import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg')

# show the BGR values for one pixel (100,100):
px = img[100,100]
print px

# show only the blue value for that pixel:
blue = img[100,100,0]
print blue

# set the pixel to white:
img[100,100] = [255,255,255]
print img[100,100]

# better way to access, set pixels based on use of numpy (optimized library):
print img.item(100,100,2) # RED value of the pixel

img.itemset((100,100,2),100) #set RED value to 100
print img.item(100,100,2)

# image attributes
# resolution and number values used for color - if grayscale, only one used
#    and only returns rows, columns
print img.shape

# total pixels (really # bytes as also includes multiply by # values for color
print img.size

# data type
print img.dtype

# extract a piece of an image
ball = img[280:340,330:390]
img_add_ball = img
img_add_ball[273:333,100:160] = ball

cv2.imwrite('messi_out.jpg',img_add_ball)

# split and recombine BGR channels
b,g,r = cv2.split(img) # split is much less efficient that actual indexing
b = img[:,:,0] # alternate extraction with indexing
img = cv2.merge((b,g,r))

# set all red values to zero
img_no_red = img
img_no_red[:,:,2] = 0
cv2.imwrite('messi_no_red.jpg',img_no_red)

BLUE = [255,0,0]

img1 = cv2.imread('opencv_logo.png')

replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()
