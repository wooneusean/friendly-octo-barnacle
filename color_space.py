import cv2 as cv

img = cv.imread('photos/cat.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)
