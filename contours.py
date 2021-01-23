import cv2 as cv
import numpy as np

img = cv.imread('photos/mahjong.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blank = np.zeros(img.shape, dtype='uint8')

blurred = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)

canny = cv.Canny(blurred, 100, 150)

# ret, thresh = cv.threshold(gray, 105, 255, cv.THRESH_BINARY)

cv.imshow('Cat', canny)

contours, hierarchies = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0, 0, 255), 1, cv.LINE_AA)

cv.imshow('Contours drawn', blank)

cv.waitKey(0)
