import numpy as np
import cv2 as cv


def nothing():
    pass


image = cv.imread('benthospic.jpg', cv.IMREAD_GRAYSCALE)
cv.createTrackbar('trackbar', 'image', 0, 255, nothing)
resized = cv.resize(image, (0, 0), None, 0.5, 0.5)
cv.imshow('resized', resized)

cv.imshow('image', image)
cv.waitKey(0)
cv.destroyAllWindows()
