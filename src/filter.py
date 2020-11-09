import cv2 as cv
import numpy as np
import os
import sys


class linearFilter(object):
    """Linear filters implemented using a opencv backend."""

    def __init__(self):
        """Empty __init__ for now."""
        pass

    def sobel(self, img, format, axis="default", k_size=3):
        """
        Take image and return the gradient computed along specified axis.

        Also compute the overall magnitude and direction of derivative. The
        input uint8 image is normalized and blurred before the gradient along x
        and y are computed. The final gradient magnitude and direction are as
        given in:
        https://docs.opencv.org/3.4/d2/d2c/tutorial_sobel_derivatives.html

        Input arguments:
        img -- Input image as a numpy array
        format -- Data type of the image array; default = CV_64F
        axis -- Gradient along "x" or "y" is computed; "default" computes both
        k_size -- Kernel size of the filter
        Returns:
        grad -- Output of img convolved with filter
        """
        # Compute the sobel derivative along x and y axis
        # A compute the overall magnitude and angle pixel-wise
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

        # Normalize and Blur the image to remove noise
        img = img/255.0
        img = cv.GaussianBlur(img, (3, 3), 0)

        # Computer the image gradients along x,y and overall
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

    def laplace(self, img, format):
        """
        Compute the Laplacian of the input image.

        Compute the Laplacian of the image to observe the edges. The input is
        taken as a uint8 and blurred and normalized before the laplacian is
        computed. Edges are considered to be points where zero-crossing occurs.

        Input argumnets:
        img -- Input image as a numpy array; dtype = uint8
        format -- Data type; default = CV_64F

        Returns:
        laplace -- Returns the laplacian of the image
        """
        # Convert to greyscale and normalize to make datatype CV_64F
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        img = img/255.0

        # Blur the image to reduce the effect of noise
        img = cv.GaussianBlur(img, (3, 3), 0)

        # Compute the Lapalacian of the image
        laplace = cv.Laplacian(img, format)

        return laplace


# All test functions for testing the functions implemented above
def sobel_test(args, filt):
    """Test whether everything is okay with the Sobel funcition."""
    base_dir = "../Data"

    # Define the params to test the function
    params = {
        'format': cv.CV_64F,
        'k_size': 5,
        'axis': 'default'
    }
    # Read the image and blur to remove noise
    img = cv.imread(os.path.join(base_dir, 'Lena.jpg'))

    # Call an instance of sobel class
    grad, dir = filt.sobel(img, **params)
    print(np.unique(grad))

    cv.imshow('frame', grad)
    cv.waitKey()

    return 1


# All test functions for testing the functions implemented above
def laplace_test(args, filt):
    """Test whether everything is okay with the Laplace funcition."""
    base_dir = "../Data"

    # Define the params to test the function
    params = {
        'format': cv.CV_64F,
    }
    # Read the image and blur to remove noise
    img = cv.imread(os.path.join(base_dir, 'Lena.jpg'))

    # Call an instance of sobel class
    grad, dir = filt.sobel(img, **params)
    print(np.unique(grad))

    cv.imshow('frame', grad)
    cv.waitKey()

    return 1


# To test if the class above is functional
if __name__ == "__main__":
    args = sys.argv[1:]

    checks = [
        (sobel_test, "Sobel filter working correctly."),
        (laplace_test, "Lapacian filter working correctly.")
    ]

    # Call an instance of sobel class
    filt = linearFilter()

    # Pass on the instance to the functions and test
    outputs = []
    for check, msg in checks:
        if check(args, filt):
            print(msg)
        else:
            print("Test failed, have a look at this function.")
