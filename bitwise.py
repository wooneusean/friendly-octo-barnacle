import cv2 as cv
from utils import rescaleFrame

img = cv.imread('photos/mahjong.png')
img = rescaleFrame(img)
cv.imshow('Mahjong', img)

cv.waitKey(0)
