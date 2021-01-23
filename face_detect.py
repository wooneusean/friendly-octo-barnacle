import cv2 as cv
import numpy as np
from utils import rescaleFrame

img = cv.imread('photos/people2.jpg')
rescaled = rescaleFrame(img, 0.5)
sample = rescaled

gray = cv.cvtColor(sample, cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(sample, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)


cv.imshow('Person', sample)

cv.waitKey(0)
