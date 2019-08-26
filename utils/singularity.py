from utils import image_postprocess


class Singularity(object):

    def __init__(self,):
        self.img_prep = image_postprocess.ImagePostprocess()
        print('Singularity initiated ...')

    def vlp_singularity(self, plate_img):
        if plate_img is not None:
            plate_H, plate_W, plate_C = plate_img.shape
            if plate_W and plate_H > 0:
                if plate_W/plate_H < 2.2:
                    # TODO: Solves double line cut problem by contour
                    ocr_img = self.img_prep.single_line_concat(plate_img, plate_H, plate_W, plate_C)
                else:
                    ocr_img = plate_img

                return ocr_img
