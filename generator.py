import glob
import os
import argparse
import cv2
import random

from generators import nonlexicon_word
from generators import license_plate
from generators import image_gen
from utils import singularity
from utils import augmentation


def init_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--numbers', type=int, help='Number of images to generate')
    parser.add_argument('--mode', type=str, help='lex, nonlex, my_plate')
    parser.add_argument('--pers_trans', type=str, help='on, off')
    parser.add_argument('--augment', type=str, help='on, off')
    parser.add_argument('--single_line', type=str, help='on, off')
    parser.add_argument('--save_dir', type=str, help='Full path to save directory, '
                        'Please include "/" at EOL')

    return parser.parse_args()


def generator(numbers, mode, pers_trans, augment, single_line, save_dir):
    number = numbers
    # lex_gen = lexicon_word.LexiconWords(number)
    # TODO: Solves lexicon words issue
    nonlex_gen = nonlexicon_word.NonlexiconWord(number)
    plate_gen = license_plate.LicensePlate(number)
    img_gen = image_gen.ImageGenerator(save_dir)
    plate_ninja = singularity.Singularity()
    plate_aug = augmentation.Augmenters()
    if mode == 'lex':
        lex_words = lex_gen.generate_words()
        print("**Lexicon Word**\n", lex_words)
        img_gen.lex_image(lex_words)
        # TODO: Lexicon words gen panda web crawler
    elif mode == 'nonlex':
        nonlex_word = nonlex_gen.generate_words()
        print("**Non-Lexicon Word**\n", nonlex_word)
    elif mode == 'my_plate':
        plate = plate_gen.plate()
        print("**License Plate**\n", plate)
        print("\n{}".format(len(plate)))
        img_gen.plate_image(plate, pers_trans)

        for n, image in enumerate(sorted(glob.glob(os.path.join(save_dir, '*.jpg')))):
            print('Postprocessing: {}'.format(n-1), end='\r')
            # print('Still going Be patient')
            img = cv2.imread(image)
            if single_line == 'on':
                img = plate_ninja.vlp_singularity(img)
            if augment == 'on':
                augmenter = [plate_aug.invert_color(img), plate_aug.salt_pepper(img)]
                img = random.choice(augmenter)
            cv2.imwrite(image, img)
        print('Done Postprocessing          ')

        # TODO: Make philippine's plates generator


if __name__ == '__main__':
    args = init_args()
    if not os.path.exists(args.save_dir):
        # Single Thread
        generator(numbers=args.numbers, mode=args.mode, pers_trans=args.pers_trans, augment=args.augment,
                  single_line=args.single_line, save_dir=args.save_dir)
    else:
        print('Destination directory exists. Please choose new directory')



