import numpy as np


def read_input(filename):
    """
    Read input; code into a binary string and the picture into 
    a int array

    Parameters
    ----------
    filename : str
        path to filename

    Returns
    -------
    str, np.ndarray
        the code for picture enhancing and array.
    """
    with open(filename, "r") as f:
        code = ""
        line = f.readline()
        while line != "\n":
            code += line.strip()
            line = f.readline()

        code = code.replace(".", "0")
        code = code.replace("#", "1")

        picture = []
        for line in f:
            line = line.strip()
            line = line.replace(".", "0")
            line = line.replace("#", "1")
            picture.append([char for char in line])

        picture = np.asarray(picture, dtype=int)

        return code, picture


class PictureEnhancer(object):
    def __init__(self, code):
        """
        Picture Enhancer taking in the code for enhancer. Depending
        on the code different modes for blinking and not blinking 
        input is there

        Parameters
        ----------
        code : string
            01 string for enhancing pictures
        """
        self.code = code
        self.padding = 3  # two does also work, 1 shouldn't
        if int(self.code[0]) == 1 and int(self.code[-1]) == 0:
            self.blinking = True
        else:
            self.blinking = False

    def augment_picture(self, picture, dark=True):
        """
        Helper function augmenting pictures

        Parameters
        ----------
        picture : np.ndarray
        dark : bool, optional
            only important if it's a blinking image, by default True

        Returns
        -------
        np.ndarray, np.ndarray
            augmented picture and new picture template
        """
        padding = self.padding
        nrows, ncols = picture.shape
        new_shape = (nrows + 2 * padding, ncols + 2 * padding)
        aug = {True: np.zeros, False: np.ones}
        if self.blinking:
            augmented_picture = aug.get(not dark)(new_shape)
            new_picture = aug.get(dark)(new_shape)
        else:
            augmented_picture = aug.get(True)(new_shape)
            new_picture = aug.get(True)(new_shape)

        augmented_picture[padding:-padding, padding:-padding] = picture
        return augmented_picture, new_picture

    def enhance_picture(self, picture, i):
        """
        Enhances a picture by padding it with a few 0s or 1s (depending
        on blinking state) and calculates the enhanced picture from code.

        Parameters
        ----------
        picture : np.ndarray
        i : wheter or not that is a light or dark blinking state

        Returns
        -------
        np.ndarray
            new picture
        """
        padding = self.padding
        nrows, ncols = picture.shape
        dark = True
        if i % 2 == 0:
            dark = False

        augmented_picture, new_picture = self.augment_picture(picture, dark=dark)

        for nrow in range(1, nrows + 2 * padding - 1, 1):
            for ncol in range(1, ncols + 2 * padding - 1, 1):
                binary = self.find_binary(augmented_picture, nrow, ncol)
                code_pos = int(binary, 2)
                new_picture[nrow, ncol] = int(self.code[code_pos])

        return new_picture

    @staticmethod
    def find_binary(picture, nrow, ncol):
        binary = ""
        for row in range(nrow - 1, nrow + 2, 1):
            for col in range(ncol - 1, ncol + 2, 1):
                binary += str(int(picture[row, col]))

        return binary
