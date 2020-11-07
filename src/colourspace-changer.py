import cv2 as cv
import os


class c_space_changer(object):
    """Functions for playing with image colourspace."""

    def __init__(self, dims):
        """Initialize c_space changer with the base directory of image data."""
        self.dims = dims

    def space_change(self, img, src_space, target_space):
        """
        Take the image, source and target space and return the corrected image.

        Input Arguments:
        img -- Input image as a umpy array
        src_space -- String with the source colourspace
        target_space -- Sting with the target colourspace

        Returns:
        img_corrected -- Colour space corrected numpy output
        """
        # Concatanate parameter to be passed into cvtColor
        param = src_space+"2"+target_space
        keyword_dict = {
            "BGR2RGB": cv.COLOR_BGR2RGB,
            "BGR2HSV": cv.COLOR_BGR2HSV,
            "BGR2GRAY": cv.COLOR_BGR2GRAY
        }

        # Convert the color using the above dict and return the same
        img_corrected = cv.cvtColor(img, keyword_dict[param])
        print("Currently printing ")
        return img_corrected


if __name__ == "__main__":

    # To test if the functions above produce expected outputs
    base_dir = "..\Data"
    img = cv.imread(os.path.join(base_dir, 'lena.jpg'))
    chng = c_space_changer(base_dir)

    c_img = chng.space_change(img, "BGR", "RGB")
    cv.imshow('frame', c_img)

    cv.waitKey()
