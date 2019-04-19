import os,glob
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
from utils import msia_plate_process
from utils import augmentation


class ImageGenerator(object):

    def __init__(self, save_path):
        self.savepath = save_path
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        self.word_background = glob.glob(os.path.join('background/word/', '*.jpg'))
        self.plate_background = glob.glob(os.path.join('background/msia/', '*.jpg'))
        self.long_plate_background = glob.glob(os.path.join('background/long_msia/', '*.jpg'))
        self.plate_font = glob.glob(os.path.join('fonts/msia/', '*.ttf'))
        self.word_font = glob.glob(os.path.join('fonts/word/', '*.ttf'))
        print("Image Generator Initiated ...")
        self.msia_processing = msia_plate_process.MsiaVLPProcessing()
        self.plate_aug = augmentation.Augmenters()

    def text_contruction(self, draw, font, text, img_w, img_h, draw_w, draw_h):
        draw.text(xy=((((img_w - draw_w) / 2)-1), ((img_h - draw_h) / 2)-1), text=text, fill=(10, 10, 10), font=font, align="center")
        draw.text(xy=((((img_w - draw_w) / 2)+1), ((img_h - draw_h) / 2)-1), text=text, fill=(10, 10, 10), font=font, align="center")
        draw.text(xy=((((img_w - draw_w) / 2)+1), ((img_h - draw_h) / 2)+1), text=text, fill=(10, 10, 10), font=font, align="center")
        draw.text(xy=((((img_w - draw_w) / 2)-1), ((img_h - draw_h) / 2)+1), text=text, fill=(10, 10, 10), font=font, align="center")
        draw.text(xy=((img_w - draw_w) / 2, (img_h - draw_h) / 2), text=text, fill=(248, 248, 248), font=font, align="center")
        # TODO: Varies image size for each generated sample
        return

    def plate_image(self, plate, pers_trans):
        for word_index in range(len(plate)):
            background = self.plate_background[np.random.randint(0, len(self.plate_background))]
            img = Image.open(background)
            img_w, img_h = img.size
            font_ = self.plate_font[np.random.randint(0, len(self.plate_font))]
            # print(len(chr(plate[word_index])))
            font = ImageFont.truetype(font=font_, size=18)
            draw = ImageDraw.Draw(img)
            draw_w, draw_h = draw.textsize(plate[word_index], font=font)
            if img_w / img_h > 2:
                self.text_contruction(draw, font, plate[word_index], img_w, img_h, draw_w, draw_h)
                # draw.text(xy=((img_w-draw_w)/2, (img_h-draw_h)/2), text=plate[word_index], font=font, align="center")
            else:
                plate1 = plate[word_index].split(maxsplit=1)[0] + '\n' + plate[word_index].split(maxsplit=1)[1]
                self.text_contruction(draw, font, plate1, img_w, img_h, draw_w, draw_h)
                # draw.text(xy=((img_w - draw_w) / 2, (img_h - draw_h) / 2), text=plate[word_index], font=font,
                #           align="center")
            # Convert PIL image to OpenCV image matrix
            cv2img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
            # Perspective Transformation
            if pers_trans == 'on':
                cv2img = self.plate_aug.persp_trans(cv2img)
            else:
                pass
            # Crop to tight license plate
            contours = self.msia_processing.dilate_contours(cv2img)
            x_min, x_max, y_min, y_max = self.msia_processing.contour_hunter(contours)
            vlp_img = cv2img[y_min:y_max, x_min:x_max]
            cv2.imwrite(self.savepath + '%06d' % word_index + '_' + plate[word_index].replace(' ', '') + '.jpg', vlp_img)
            # # PIL image save for unprocessed image
            # img.save(self.savepath + '%06d' % word_index + '_' + plate[word_index].replace(' ', '') + '.jpg')
            # print("Plate {0} @ word_index {1}".format(plate[word_index], word_index))

    def lex_image(self, lex):
        for word_index in range(len(lex)):
            background = self.word_background[np.random.randint(0, len(self.word_background))]
            img = Image.open(background)
            img_w, img_h = img.size
            font_ = self.word_font[np.random.randint(0, len(self.word_font))]
            font = ImageFont.truetype(font=font_, size=15)
            draw = ImageDraw.Draw(img)
            draw_w, draw_h = draw.textsize(lex[word_index], font=font)
            self.text_contruction(draw, font, lex[word_index], img_w, img_h, draw_w, draw_h)
            img.save(self.savepath + '%06d' % word_index + '_' + lex[word_index].replace(' ', '') + '.jpg')
            # print("Plate {0} @ word_index {1}".format(plate[word_index], word_index))
