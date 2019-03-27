from shapedetector import ShapeDetector
import cv2 as cv
import imutils

image = cv.imread('benthospic.jpg')
grey = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# convert the image to grayscale, blur it slightly,
# and threshold it
blurred = cv.GaussianBlur(grey, (5, 5), 0)
thresh = cv.threshold(blurred, 60, 255, cv.THRESH_BINARY_INV)[1]

# find contours in the thresholded image and initialize the
# shape detector
cnts = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = ShapeDetector()
# loop over the contours
for c in cnts:

    shape = sd.detect(c)
    cv.drawContours(image, [c], 0, (0, 255, 0), 2)
    cv.imshow('contours', image)

sd.print_figures()
cv.waitKey(0)

