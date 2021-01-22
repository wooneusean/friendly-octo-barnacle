import cv2 as cv
import numpy as np
from utils import rescaleCenter, getCenter

# blank = np.zeros((500, 500), dtype='uint8')
# cv.imshow('Blank', blank)

img = cv.imread('photos/cat.jpg')

x1, y1, x2, y2 = rescaleCenter(img.shape[1], img.shape[0])

cv.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0),
             thickness=2, lineType=cv.LINE_AA)
# cv.imshow('Rectangle', img)

centerPoint = getCenter(img.shape[1],
                        img.shape[0])

cv.circle(img, centerPoint, 100, (0, 255, 0), thickness=2, lineType=cv.LINE_AA)
# cv.imshow('Circle', img)

cv.line(img, (x1, y1), (x2, y2), (255, 0, 0), thickness=2, lineType=cv.LINE_AA)
cv.line(img, (x1, y2), (x2, y1), (255, 0, 0), thickness=2, lineType=cv.LINE_AA)

cv.putText(img, 'Yeet', centerPoint, cv.FONT_HERSHEY_TRIPLEX,
           1.0, (255, 255, 255), thickness=1, lineType=cv.LINE_AA)

cv.imshow('Image', img)
cv.waitKey(0)
