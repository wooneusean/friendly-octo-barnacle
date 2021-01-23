import cv2 as cv
import numpy as np
from utils import rescaleFrame

img = cv.imread('photos/people.jpg')
rescaled = rescaleFrame(img, 0.5)

cv.imshow('Person', rescaled)


cv.waitKey(0)
