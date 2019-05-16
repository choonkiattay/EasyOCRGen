import glob
import os
import argparse
import cv2
import random
from utils import augmentation
from utils import singularity
from generators import image_gen
from utils import image_preprocess


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--imitatee_dir', type=str, help='Full path to imitatee directory, '
                        'Please include "/" at EOL')
    parser.add_argument('--pers_trans', type=str, help='on, off')
    parser.add_argument('--augment', type=str, help='on, off')
    parser.add_argument('--grayscale', type=str, help='on, off')
    parser.add_argument('--single_line', type=str, help='on, off')
    parser.add_argument('--save_dir', type=str, help='Full path to save directory, '
                        'Please include "/" at EOL')
    parser.print_help()

    return parser.parse_args()


def imitator(imitatee_dir, pers_trans, augment, grayscale, single_line, save_dir):
    plate_ninja = singularity.Singularity()
    plate_aug = augmentation.Augmenters()
    img_preproc = image_preprocess.ImagePreprocess()
    imitatee=[]
    img_gen = image_gen.ImageGenerator(save_dir)
    for imitatee_file in glob.glob(os.path.join(imitatee_dir, '*.jpg')):
        imitatee_name = imitatee_file.split('/')[-1].split('.')[0].split('_')[-1]
        for index, character in enumerate(imitatee_name):
            if character.isdigit():
                imitatee_name = imitatee_name[:index] + ' ' + imitatee_name[index:]
                break
        imitatee.append(imitatee_name)
    print(imitatee)
    print("\n{}".format(len(imitatee)))
    img_gen.plate_image(imitatee, pers_trans)
    for n, image in enumerate(sorted(glob.glob(os.path.join(save_dir, '*.jpg')))):
        print('Postprocessing: {}'.format(n - 1), end='\r')
        # print('Still going Be patient')
        img = cv2.imread(image)
        if single_line == 'on':
            img = plate_ninja.vlp_singularity(img)
        if augment == 'on':
            augmenter = [plate_aug.invert_color(img), plate_aug.salt_pepper(img), plate_aug.random_resize(img),
                         plate_aug.plate_blur(img)]
            img = random.choice(augmenter)
        if grayscale == 'on':
                img = img_preproc.gray(img)
        cv2.imwrite(image, img)
    print('Done Postprocessing          ')


if __name__ == '__main__':
    args = init_args()
    if not os.path.exists(args.save_dir):
        imitator(imitatee_dir=args.imitatee_dir, save_dir=args.save_dir, pers_trans=args.pers_trans,
                 augment=args.augment, grayscale=args.grayscale, single_line=args.single_line)
    else:
        print('Destination directory exists. Please choose new directory')


