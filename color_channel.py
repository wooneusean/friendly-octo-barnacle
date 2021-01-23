import cv2 as cv
from utils import rescaleFrame
import numpy as np

img = cv.imread('photos/mahjong.png')
rescaled = rescaleFrame(img)
cv.imshow('Mahjong', rescaled)

b, g, r = cv.split(rescaled)

blank = np.zeros(rescaled.shape[:2], dtype='uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('b', blue)
cv.imshow('g', green)
cv.imshow('r', red)

cv.waitKey(0)
