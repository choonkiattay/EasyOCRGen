import numpy as np
import cv2


class ImagePostprocess(object):

    def __init__(self):
        # Set width to be general length for consistent compute result
        self.final_w = 200
        print("Image Pre-process Engine ... Checked")

    def check_size(self, img_h, img_w):
        if img_w < self.final_w:
            diff_w = self.final_w - img_w
            return img_h, img_w

    def post_padding(self, img):
        img_h, img_w, img_c = img.shape
