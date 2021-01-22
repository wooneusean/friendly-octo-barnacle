import cv2 as cv

img = cv.imread('photos/cat.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)

dilated = cv.dilate(canny, (7, 7), iterations=1)

eroded = cv.erode(dilated, (7, 7), iterations=1)

resize = cv.resize(eroded, (500, 500), interpolation=cv.INTER_CUBIC)

cropped = resize[50: 200, 200:400]

cv.imshow('Image', cropped)

cv.waitKey(0)
