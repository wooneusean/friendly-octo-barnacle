import cv2 as cv


def getCenter(*dimensions):
    return (dimensions[0]//2, dimensions[1]//2)


def rescaleCenter(*dimensions, scale=0.5):
    x1 = int(dimensions[0]//2 - (dimensions[0]//2*scale))
    y1 = int(dimensions[1]//2 - (dimensions[1]//2*scale))
    x2 = int(dimensions[0]//2 + (dimensions[0]//2*scale))
    y2 = int(dimensions[1]//2 + (dimensions[1]//2*scale))

    return (x1, y1, x2, y2)


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
