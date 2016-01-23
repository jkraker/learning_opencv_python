import numpy as np
import os
import cv2
import sys

# noisy function from Shubham Pachori on stack overflow
# Parameters
#----------
#image : ndarray
#    Input image data. Will be converted to float.
#mode : str
#    One of the following strings, selecting the type of noise to add:

#    'gauss'     Gaussian-distributed additive noise.
#    'poisson'   Poisson-distributed noise generated from the data.
#    's&p'       Replaces random pixels with 0 or 1.
#    'speckle'   Multiplicative noise using out = image + n*image,where
#                n,is uniform noise with specified mean & variance.

def noisy(noise_typ,image):

    if noise_typ == "gauss":
        row,col,ch= image.shape
        mean = 0
        #var = 0.1
        #sigma = var**0.5
        gauss = np.random.normal(mean,10,(row,col,ch))
        gauss = gauss.reshape(row,col,ch)
        noisy = image + gauss
        return noisy
    elif noise_typ == "s&p":
        row,col,ch = image.shape
        s_vs_p = 0.5
        amount = 0.004
        out = image
        # Salt mode
        num_salt = np.ceil(amount * image.size * s_vs_p)
        coords = [np.random.randint(0, i - 1, int(num_salt))
                  for i in image.shape]
        out[coords] = 1

        # Pepper mode
        num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
        coords = [np.random.randint(0, i - 1, int(num_pepper))
                  for i in image.shape]
        out[coords] = 0
        return out
    elif noise_typ == "poisson":
        vals = len(np.unique(image))
        vals = 2 ** np.ceil(np.log2(vals))
        noisy = np.random.poisson(image * vals) / float(vals)
        return noisy
    elif noise_typ =="speckle":
        row,col,ch = image.shape
        gauss = np.random.randn(row,col,ch)
        gauss = gauss.reshape(row,col,ch)        
        noisy = image + image * gauss
        return noisy

if len(sys.argv) != 4:
    print "usage:",sys.argv[0],"<image> <1|2|3|4 (noise type)> <output name>"
    print "    noise types:"
    print "        1: Gaussian"
    print "        2: salt and pepper"
    print "        3: poisson"
    print "        4: speckle"
    sys.exit(0)

noisy_img_name = sys.argv[3]

img = cv2.imread(sys.argv[1])
if img == None:
    print "invalid image:",sys.argv[1]
    sys.exit(1)

noise_type = 'gauss' # default type - '1'
if sys.argv[2] == '1':
    pass
elif sys.argv[2] == '2':
    noise_type = 's&p'
elif sys.argv[2] == '3':
    noise_type = 'poisson'
elif sys.argv[2] == '4':
    noise_type = 'speckle'
else:
    print "invalid noise type:",sys.argv[2]
    sys.exit(1)

noisy_img = noisy(noise_type, img)

cv2.imwrite(noisy_img_name, noisy_img)
