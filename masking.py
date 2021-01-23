import cv2 as cv
import numpy as np
from utils import rescaleFrame

img = cv.imread('photos/mahjong.png')
rescaled = rescaleFrame(img)

blank = np.zeros(rescaled.shape[:2], dtype='uint8')

mask = cv.rectangle(
    blank, (rescaled.shape[1]//2-600, rescaled.shape[0]//2+275), (rescaled.shape[1]//2+500, rescaled.shape[0]//2+400), 255, -1)

masked = cv.bitwise_and(rescaled, rescaled, mask=mask)

cv.imshow('Blank Image', masked)

cv.waitKey(0)
