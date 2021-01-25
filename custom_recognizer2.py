import cv2 as cv
import numpy as np
import os
from utils import rescale_frame, find_image

TEMPLATE_DIR = r'photos\tiles'

img = cv.imread(r'photos\mahjong.png')
rescaled = rescale_frame(img)

# Template match for multiple
for tile in os.listdir(TEMPLATE_DIR):
    path_to_tile = os.path.join(TEMPLATE_DIR, tile)
    print(path_to_tile)

    correct_scale = -1

    template = cv.imread(path_to_tile)
    for scale in np.linspace(0.5, 1, 10)[::-1]:

        resized_template = rescale_frame(template, scale)
        gray_template = cv.cvtColor(resized_template, cv.COLOR_BGR2GRAY)
        w, h = gray_template.shape[::-1]

        res = cv.matchTemplate(sample, gray_template, cv.TM_CCOEFF_NORMED)
        threshold = 0.9
        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            cv.rectangle(rescaled, pt, (pt[0]+w, pt[1] + h), (0, 0, 255), 2)
            cv.putText(rescaled, tile[:-4], (pt[0], pt[1]-12),
                       cv.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 1, cv.LINE_AA)


cv.imshow('Mahjong', rescaled)

cv.waitKey(0)


# # Template match single but loop
# for tile in os.listdir(TEMPLATE_DIR):
#     path_to_tile = os.path.join(TEMPLATE_DIR, tile)
#     template = cv.imread(path_to_tile)
#     rescaled_template = rescale_frame(template)
#     try:
#         x, y = find_image(rescaled, rescaled_template)
#         print((x, y))
#     except:
#         print('not found')
