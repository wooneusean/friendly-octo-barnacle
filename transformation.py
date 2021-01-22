import cv2 as cv
import numpy as np
from mss import mss


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


img = cv.imread('photos/cat.jpg')

# translate
# translated = translate(img, 100, 100)
# cv.imshow('Image', translated)

# rotate
# rotated = rotate(img, 45)
# cv.imshow('Image', rotated)

# resizing
# resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Image', resized)

# flipping
flipneg = cv.flip(img, -1)
flipzero = cv.flip(img, 0)
flipone = cv.flip(img, 1)
cv.imshow('flipneg', flipneg)
cv.imshow('flipzero', flipzero)
cv.imshow('flipone', flipone)

# Cropping
cropped = img[200:600, 200:600]
cv.imshow('cropped', cropped)

cv.waitKey(0)
