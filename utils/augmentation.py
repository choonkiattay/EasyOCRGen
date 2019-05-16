import numpy as np
import random
from imgaug import augmenters as iaa


class Augmenters(object):

    def __init__(self):
        self.sometimes = lambda aug: iaa.Sometimes(0.5, aug)
        print('Augmenter initiated ...')

    def invert_color(self, img, power=1):
        seq = iaa.Sequential([iaa.Invert(power, per_channel=False)])
        img1 = np.transpose(img, (2, 0, 1))
        img_aug1 = seq.augment_images(img1)
        img_aug = np.transpose(img_aug1, (1, 2, 0))
        return img_aug

    def random_resize(self, img):
        power = round(random.uniform(0.5, 2.0), 2)
        seq = iaa.Sequential([iaa.Resize(power)])
        img1 = np.transpose(img, (2, 0, 1))
        img_aug1 = seq.augment_images(img1)
        img_aug = np.transpose(img_aug1, (1, 2, 0))
        return img_aug

    def plate_persp_trans(self, img, p1=0.05, p2=0.05):
        seq = iaa.Sequential([iaa.PerspectiveTransform(scale=(p1, p2), deterministic=True, keep_size=True)])
        img_aug = seq.augment_image(img)
        return img_aug

    def plate_blur(self, img, power=1):
        seq = iaa.Sequential([iaa.GaussianBlur(power)])
        img1 = np.transpose(img, (2, 0, 1))
        img_aug1 = seq.augment_images(img1)
        img_aug = np.transpose(img_aug1, (1, 2, 0))
        return img_aug

    def word_persp_trans(self, img, p1=0.1, p2=0.1):
        seq = iaa.Sequential([iaa.PerspectiveTransform(scale=(p1, p2), deterministic=True, keep_size=True)])
        img_aug = seq.augment_image(img)
        return img_aug

    def salt_pepper(self, img, power=0.05):
        seq = iaa.Sequential([iaa.SaltAndPepper(power, per_channel=False)])
        img1 = np.transpose(img, (2, 0, 1))
        img_aug1 = seq.augment_images(img1)
        img_aug = np.transpose(img_aug1, (1, 2, 0))
        return img_aug
