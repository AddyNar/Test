import cv2 as cv
from cspace_change.py import ColourSpaceChanger
import os

class maskGen(object):
    """
    Class which contains various image mask generation functions.
    """
    def __init__(dims):
        self.dims = dims

    def colour_mask(slf, img, upper_thresh, lower_thresh):
        """
        Generate a mask for three channel images. By default, images channels
        are assumed to be in (B,G,R) as is default in OpenCV.

        Input arguments:
        img -- input image; default channel is assumed to be (B,G,R)
        upper_thresh -- Upper bound for valid BGR combination
        lower_thresh -- Lower bound for valid BGR combination
        """
        # Convert colourspace from BGR to HSV
        spc = ColourSpaceChanger(self.dims)
        hsv = spc.space_change(img, "BGR", "HSV")

        # Generate a mask with the given RGB bounds
        mask = cv.inRange(hsv, upper_thresh, lower_thresh)

        # Bitwise-AND mask and original imagw
        res = cv.bitwise_and(img, img, mask=mask)

        return res

    def gray_thresh_mask():
        """

        """
        return

    def otsu_mask():
        """

        """
        return


if __name__ == "__main__":
    base_dir = "../Data"
    img = cv.imread(os.path.join(base_dir, "lena.jpg"))
    mask = maskGen(dims=(256, 256))
    out = mask.colour_mask()
    cv.imshow(out)
    cv.waitKey()
