import cv2 as cv
import numpy as np
from utils import rescale_frame

img = cv.imread('photos/mahjong.png')
rescaled = rescale_frame(img, 0.5)
cv.imshow('Mahjong', rescaled)

gray = cv.cvtColor(rescaled, cv.COLOR_BGR2GRAY)

# # Laplacian
# lap = cv.Laplacian(gray, cv.CV_64F)
# lap = np.uint8(np.abs(lap))
# cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel', combined_sobel)

canny = cv.Canny(gray, 100, 125)
cv.imshow('Canny', canny)

cv.waitKey(0)
