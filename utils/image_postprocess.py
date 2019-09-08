import numpy as np
import cv2


class ImagePostprocess(object):

    def __init__(self):
        # Set width to be general length for consistent compute result
        self.final_w = 200
        print("Image Pre-process Engine ... Checked")

    def gray(self, img):
        img = np.array(img, dtype=np.uint8)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return gray

    def single_line_concat(self, rgb, h, w, c):
        # smaller, the nearer
        edge_compensate = 10
        center_h = int(h/2)
        h_px = int(h)
        w_px = int(w)
        top = rgb[0:center_h, 0:w_px]
        bottom = rgb[center_h:h_px, 0:w_px]
        if top.shape[0] > bottom.shape[0]:
            diff = int(top.shape[0] - bottom.shape[0])
            bottom = cv2.copyMakeBorder(bottom, diff, 0, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))
        elif bottom.shape[0] > top.shape[0]:
            diff = int(bottom.shape[0] - top.shape[0])
            top = cv2.copyMakeBorder(top, diff, 0, 0, 0, cv2.BORDER_CONSTANT, value=(0, 0, 0))
        # print(top.shape, bottom.shape)
        # print(h, w)
        concat_img = np.concatenate((top, bottom), axis=1)
        concat_h, concat_w, concat_c = concat_img.shape
        center_concat_h = int(concat_h/2)
        gray = cv2.cvtColor(concat_img, cv2.COLOR_BGR2GRAY)
        _, bw_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        kernel_dilate = np.ones((3, 3), np.uint8)
        dilate_img = cv2.dilate(bw_img, kernel_dilate, iterations=2)
        concat_di_middle = dilate_img[center_concat_h:center_concat_h+1, 0:concat_w]
        # normalize cv mat 255 to 1
        concat_di_middle = cv2.normalize(concat_di_middle, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX,
                                         dtype=cv2.CV_32F)
        left_edge = int((concat_w/2)-edge_compensate)
        right_edge = int((concat_w/2)+edge_compensate)
        white_contour = []
        # convert cv mat to np array
        concat_array = np.asarray(concat_di_middle[0], dtype=np.int8)
        # find white contour location
        for i, px in enumerate(concat_array):
            if px == 1:
                white_contour.append(i)
                if len(white_contour) > 2:
                    if (white_contour[-1] - white_contour[-2]) > 30:
                        left_edge = white_contour[-2]
                        right_edge = white_contour[-1]
                        # print (white_contour[-1], white_contour[-2])
        left = concat_img[0:concat_h, 0:left_edge+edge_compensate]
        right = concat_img[0:concat_h, right_edge-edge_compensate:concat_w]
        concat_img = np.concatenate((left, right), axis=1)
        return concat_img

    def check_size(self, img_w):
        if img_w < self.final_w:
            diff_w = self.final_w - img_w
        else:
            diff_w = img_w
        return diff_w

    def post_padding(self, img):
        img_h, img_w, img_c = img.shape
        diff_w = self.check_size(img_w)
        half_diff_w = int(round(diff_w/2))
        one_side_pad = np.zeros(img_h*half_diff_w*img_c).reshape(img_h, half_diff_w, img_c)
        # dark grey padding
        one_side_pad = 25*(one_side_pad + 1)
        # print("img: {}, pad: {}, ".format(img.shape, one_side_pad.shape))
        pad_plate = np.concatenate((one_side_pad, img, one_side_pad), axis=1)
        return pad_plate