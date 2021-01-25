import cv2 as cv
import numpy as np
from utils import rescale_frame

img = cv.imread('photos/mahjong.png')
rescaled = rescale_frame(img)
# cv.imshow('Mahjong', rescaled)

gray = cv.cvtColor(rescaled, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Simple thresholding
threshold, threshed_img = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Simple Threshold', threshed_img)
threshold, threshed_inv = cv.threshold(gray, 125, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Threshold Inverse', threshed_inv)

# Adaptive Thresholding
# Can either use
# cv.ADAPTIVE_THRESH_GAUSSIAN_C or
# cv.ADAPTIVE_THRESH_MEAN_C
adaptive_thresh = cv.adaptiveThreshold(
    gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 7)

cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)
