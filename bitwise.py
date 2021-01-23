import cv2 as cv
import numpy as np
from utils import rescaleFrame

# img = cv.imread('photos/mahjong.png')
# rescaled = rescaleFrame(img)
# cv.imshow('Mahjong', rescaled)

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30),
                         (370, 370), 255, -1, cv.LINE_AA)

circle = cv.circle(blank.copy(), (200, 200), 195, 255, -1, cv.LINE_AA)

cv.imshow('Circle', circle)
cv.imshow('Rect', rectangle)

# bitwise AND --> intersection regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# bitwise OR --> non intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# bitwise XOR --> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT --> flip bits
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT', bitwise_not)


cv.waitKey(0)
