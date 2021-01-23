import cv2 as cv
import numpy as np
from utils import rescaleFrame

img = cv.imread('photos/people.jpg')
rescaled = rescaleFrame(img)
sample = rescaled

cv.imshow('Mahjong', sample)


cv.waitKey(0)
