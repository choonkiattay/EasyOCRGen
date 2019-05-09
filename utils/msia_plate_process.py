import cv2
import numpy as np


class MsiaVLPProcessing(object):

    def __init__(self):
        print('Malaysia license plate processing initiated')

    def dilate_contours(self, img):
        kernel = np.ones((3, 3), np.uint8)
        roi_img = cv2.dilate(img, kernel, iterations=6)

        imgray = cv2.cvtColor(roi_img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
        contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def erode_contours(self, img):
        kernel = np.ones((5, 5), np.uint8)
        roi_img = cv2.erode(img, kernel, iterations=10)

        imgray = cv2.cvtColor(roi_img, cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
        contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        return contours

    def contour_hunter(self, contours):
        con = []
        con_points = []
        x_points = []
        y_points = []
        con_count = len(contours)
        # print(con_count)
        for count, point in enumerate(contours):
            # print('Contour count: {}'.format(count))
            # print('Contour points: {}'.format(len(point)))
            con.append(len(point))
        target_contour = np.argmax(con)

        for x in contours[target_contour]:
            add = np.sum(x)
            y_points.append(x[0][1])
            x_points.append(x[0][0])
            con_points.append(add)

        x_min_abs = x_points[int(np.argmin(x_points))]
        x_max_abs = x_points[int(np.argmax(x_points))]
        y_min_abs = y_points[int(np.argmin(y_points))]
        y_max_abs = y_points[int(np.argmax(y_points))]

        return x_min_abs, x_max_abs, y_min_abs, y_max_abs

