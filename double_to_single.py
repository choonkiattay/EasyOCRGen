import glob
import os
import argparse
import cv2
import random

from utils import singularity
from utils import augmentation
from utils import image_postprocess

def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--double_path', type=str, help='Full path for dataset, / at EOF')
    parser.add_argument('--single_path', type=str, help='Full path for dataset, / at EOF')

    parser.print_help()

    return parser.parse_args()

if __name__ == '__main__':

    plate_ninja = singularity.Singularity()
    
    args = init_args()
    if not os.path.exists(args.single_path):
            os.makedirs(args.single_path)
    if os.path.exists(args.double_path):
        for doubleline in glob.glob(os.path.join(args.double_path, '*.jpg')):
            img_dl = cv2.imread(doubleline)
            singleline = plate_ninja.vlp_singularity(img_dl)
            filename_sl = args.single_path + doubleline.split('/')[-1]
            cv2.imwrite(filename_sl, singleline)
        print('[FINISH] DOUBLE LINE -> SINGLE LINE')

    else:
        print('Double line plate directory not exists. Please select valid directory')