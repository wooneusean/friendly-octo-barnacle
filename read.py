import cv2 as cv
from rescale import rescaleFrame

img = cv.imread('photos/cat.jpg')

img = rescaleFrame(img)

cv.imshow('Cat', img)

cv.waitKey(0)
