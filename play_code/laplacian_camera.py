import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    grayscale = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    edges = cv2.Laplacian(grayscale,cv2.CV_64F)

    cv2.imshow('frame',frame)
    cv2.imshow('grayscale',grayscale)
    cv2.imshow('edges',edges)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
