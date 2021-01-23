import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

from utils import rescaleFrame

img = cv.imread('photos/mahjong.png')
rescaled = rescaleFrame(img)

# Grayscale Histogram
gray = cv.cvtColor(rescaled, cv.COLOR_BGR2GRAY)

blank = np.zeros(rescaled.shape[:2], dtype='uint8')


circle = cv.circle(
    blank, (rescaled.shape[1]//2, rescaled.shape[0]//2), 100, 255, -1)

mask = cv.bitwise_and(gray, gray, mask=circle)

cv.imshow('Mahjong', mask)

gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 255])
plt.show()

# # Colour Histogram
# blank = np.zeros(rescaled.shape[:2], dtype='uint8')

# mask = cv.circle(
#     blank, (rescaled.shape[1]//2, rescaled.shape[0]//2), 100, 255, -1)

# masked = cv.bitwise_and(rescaled, rescaled, mask=mask)

# cv.imshow('Mahjong', masked)

# plt.figure()
# plt.title('Color Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')

# colors = ('b', 'g', 'r')
# for i, col in enumerate(colors):
#     hist = cv.calcHist([rescaled], [i], mask, [256], [0, 256])
#     plt.plot(hist, color=col)
#     plt.xlim([0, 256])

# plt.show()


cv.waitKey(0)
