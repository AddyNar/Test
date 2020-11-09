import cv2 as cv
import numpy as np
import os
import sys

class linearFilter(object):
    """
    """

    def sobel(self, img, format, axis="default", k_size=3):
        """
        Take image and return the gradient computed along specified axis.

        Input arguments:
        img -- Input image as a numpy array
        format -- Value formal of the numpy array
        axis -- Gradient along "x" or "y" is computed; "default" computes both
        k_size -- Kernel size of the filter
        Returns:
        grad -- Output of img convolved with filter
        """
        # Compute the sobel derivative along x and y axis
        # A computer the overall magnitude and angle pixel-wise
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Blur to remove noise in the image
        # img = cv.G
        sobelx = cv.Sobel(img, format, 1, 0, k_size)
        sobely = cv.Sobel(img, format, 0, 1, k_size)
        sobel_mag = np.sqrt(np.square(sobelx)+np.square(sobely))
        sobel_dir = np.arctan(sobel_mag)

        # Used to return depending on what the user wants
        grad = {
            'x': (sobelx, 0),
            'y': (sobely, 0),
            'default': (sobel_mag, sobel_dir)
        }

        return grad[axis]


def sobel_test(fname):
    """
    Test whether everything is okay with the sobel funcition
    """
    base_dir = "../Data"

    #Define the params to test the function

    # Read the image and blur to remove noise
    img = cv.imread(os.path.join(base_dir, "Lena.jpg"))
    img = cv.GaussianBlur(img, (3,3), 0)

    # Call an instance of sobel class
    filt = linearFilter()
    grad, dir = filt.sobel(img, cv.CV_16S, axis='default', k_size=3)
    print(np.unique(grad))
    cv.imshow('frame', grad)
    cv.waitKey()
# To test if the class above is functional
if __name__ == "__main__":
    args = sys.argv[1:]
    sobel_test()
