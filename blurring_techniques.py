import cv2 as cv
from utils import rescale_frame

img = cv.imread('photos/noisy.png')
rescaled = rescale_frame(img, 1)

# Averaging
average = cv.blur(rescaled, (7, 7))
cv.imshow('Average', average)

# Gaussian
gauss = cv.GaussianBlur(rescaled, (7, 7), 0)
cv.imshow('Gaussian', gauss)

# Median
median = cv.medianBlur(rescaled, 3)
cv.imshow('Median', median)

# Bilateral
bilateral = cv.bilateralFilter(rescaled, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
