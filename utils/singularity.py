from utils import image_preprocess


class Singularity(object):

    def __init__(self,):
        self.img_prep = image_preprocess.ImagePreprocess()
        print('Singularity initiated ...')

    def vlp_singularity(self, plate_img):
        if plate_img is not None:
            plate_H, plate_W, plate_C = plate_img.shape
            if plate_W and plate_H > 0:
<<<<<<< HEAD
                if plate_W/plate_H < 2.2:
=======
                if plate_W/plate_H < 2.0:
>>>>>>> cef326851f4ec4923e2abf3c6758d468f8c52294
                    # TODO: Solves double line cut problem by contour
                    ocr_img = self.img_prep.concat(plate_img, plate_H, plate_W, plate_C)
                else:
                    ocr_img = plate_img

                return ocr_img
