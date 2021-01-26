from mss import mss
import cv2 as cv
import numpy as np
import os
from utils import rescale_frame, points_are_close, named_rectangle

# Template match single but loop
# for tile in os.listdir(TEMPLATE_DIR):
#     path_to_tile = os.path.join(TEMPLATE_DIR, tile)
#     print(path_to_tile)

#     template = cv.imread(path_to_tile)
#     resized_template = rescale_frame(template)
#     gray_template = cv.cvtColor(resized_template, cv.COLOR_BGR2GRAY)
#     w, h = gray_template.shape[::-1]

#     res = cv.matchTemplate(sample, gray_template, cv.TM_CCOEFF_NORMED)
#     min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)

#     top_left = max_loc
#     bottom_right = (top_left[0]+w, top_left[1]+h)

#     cv.rectangle(rescaled, top_left, bottom_right,
#                  (0, 0, 255), 2, cv.LINE_AA)
#     cv.putText(rescaled, tile[:-4], (top_left[0], top_left[1]-12),
#                cv.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), 1, cv.LINE_AA)

mon = {'top': 1080 - 250, 'left': 0, 'width': 1920, 'height': 250}
TEMPLATE_DIR = r'photos\tiles'

template_imgs = {}

for tile in os.listdir(TEMPLATE_DIR):
    path_to_tile = os.path.join(TEMPLATE_DIR, tile)
    template = cv.imread(path_to_tile)
    rescaled_template = rescale_frame(template)
    gray_template = cv.cvtColor(rescaled_template, cv.COLOR_BGR2GRAY)
    template_imgs[tile[:-4]] = gray_template

window_name = "Main View"

with mss() as sct:
    while True:
        screen = np.array(sct.grab(mon))
        rescaled_screen = rescale_frame(screen)
        gray_screen = cv.cvtColor(rescaled_screen, cv.COLOR_BGR2GRAY)
        sample = gray_screen

        # Template match for multiple
        for tile_name in template_imgs:
            w, h = template_imgs[tile_name].shape[::-1]

            res = cv.matchTemplate(
                sample, template_imgs[tile_name], cv.TM_CCOEFF_NORMED)
            threshold = 0.9
            loc = np.where(res >= threshold)
            prev_pt = []
            for pt in zip(*loc[::-1]):
                if prev_pt:
                    if not points_are_close(pt, prev_pt, w-5):
                        named_rectangle(rescaled_screen,
                                        tile_name, pt, (w, h))
                else:
                    named_rectangle(rescaled_screen,
                                    tile_name, pt, (w, h))
                prev_pt = pt

        cv.imshow(window_name, rescaled_screen)

        if cv.waitKey(25) & 0xFF == ord('q'):
            cv.destroyAllWindows()
            break

# for tile in os.listdir(TEMPLATE_DIR):
#     path_to_tile = os.path.join(TEMPLATE_DIR, tile)
#     print(path_to_tile)

#     template = cv.imread(path_to_tile)
#     resized_template = rescale_frame(template)
#     gray_template = cv.cvtColor(resized_template, cv.COLOR_BGR2GRAY)
#     w, h = gray_template.shape[::-1]

#     res = cv.matchTemplate(sample, gray_template, cv.TM_CCOEFF_NORMED)
#     threshold = 0.9
#     loc = np.where(res >= threshold)
#     for pt in zip(*loc[::-1]):
#         cv.rectangle(rescaled, pt, (pt[0]+w, pt[1] + h), (0, 0, 255), 2)
#         cv.putText(rescaled, tile[:-4], (pt[0], pt[1]-12),
#                    cv.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), x, cv.LINE_AA)

# cv.imshow('Mahjong', rescaled)

# cv.waitKey(0)
