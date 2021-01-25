import cv2 as cv
import numpy as np
from utils import rescale_frame

img = cv.imread('photos/mahjong.png')
rescaled = rescale_frame(img)
cv.imshow('Mahjong', rescaled)


cv.waitKey(0)
