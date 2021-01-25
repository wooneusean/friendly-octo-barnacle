import cv2 as cv
import numpy as np


def get_center(*dimensions):
    return (dimensions[0]//2, dimensions[1]//2)


def rescale_center(*dimensions, scale=0.5):
    x1 = int(dimensions[0]//2 - (dimensions[0]//2*scale))
    y1 = int(dimensions[1]//2 - (dimensions[1]//2*scale))
    x2 = int(dimensions[0]//2 + (dimensions[0]//2*scale))
    y2 = int(dimensions[1]//2 + (dimensions[1]//2*scale))

    return (x1, y1, x2, y2)


def rescale_frame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def points_are_close(pt1, pt2, max_deviation):
    x = np.sqrt(np.power((pt1[0] - pt2[0]), 2) +
                np.power((pt1[1] - pt2[1]), 2))

    if (x > max_deviation):
        return False
    else:
        return True


def named_rectangle(img, text, pt, pt2):
    cv.rectangle(
        img, pt, (pt[0]+pt2[0], pt[1] + pt2[1]), (0, 0, 255), 2)
    cv.putText(img, text, (pt[0], pt[1]-12),
               cv.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 1, cv.LINE_AA)


def find_image(im, tpl):
    """Something like cv.matchTemplate but supposed to be faster
I can't get it to work so I'm just leaving this in here
in case in the future it works for some reason... 

    Args:
        im (data u get from cv.imread() idfk): this would be the image the template be put on
        tpl (data u get from cv.imread() idfk): this be the template

    Raises:
        Exception: it throw error if it no found shit

    Returns:
        tuple(int, int): x and y coordinates respectively
    """
    im = np.atleast_3d(im)
    tpl = np.atleast_3d(tpl)
    H, W, D = im.shape[:3]
    h, w = tpl.shape[:2]

    # Integral image and template sum per channel
    sat = im.cumsum(1).cumsum(0)
    tplsum = np.array([tpl[:, :, i].sum() for i in range(D)])

    # Calculate lookup table for all the possible windows
    iA, iB, iC, iD = sat[:-h, :-w], sat[:-h, w:], sat[h:, :-w], sat[h:, w:]
    lookup = iD - iB - iC + iA
    # Possible matches
    possible_match = np.where(np.logical_and.reduce(
        [lookup[..., i] == tplsum[i] for i in range(D)]))

    # Find exact match
    for y, x in zip(*possible_match):
        if np.all(im[y+1:y+h+1, x+1:x+w+1] == tpl):
            return (y+1, x+1)

    raise Exception("Image not found")
