import numpy as np


def read_input(inputfile):
    """
    Read in input:
    x1,y1 -> x2,y2

    split at the -> and then at the commas

    Parameters
    ----------
    inputfile : str
        path to input file

    Returns
    -------
    np.array
        three dimensional array holding x y values in each row. First row
        start second row finish
    """
    ventlines = []
    with open(inputfile, "r") as f:
        for line in f:
            line = line.split("->")
            line = [item.split(",") for item in line]
            start, stop = [(int(item[0]), int(item[1])) for item in line]
            ventlines.append((start, stop))

    ventlines = np.asarray(ventlines)
    return ventlines


def find_xy_max(ventlines):
    """
    Return the maximal x and y values found.

    Parameters
    ----------
    ventlines : three dimensional array

    Returns
    -------
    tuple of int
        maximal x and y value
    """
    x_max = np.amax(ventlines[:, :, 0])
    y_max = np.amax(ventlines[:, :, 1])

    return x_max + 1, y_max + 1


class Map(object):
    def __init__(self, rows, columns):
        """
        Map object of the ocean floor with methods to mark vent lines

        Parameters
        ----------
        rows : maximal x position
        columns : maximal y position
        """
        self.map = np.zeros((rows, columns))

    def mark_vent(self, array):
        """
        Checks if a vent line is horizontal, vertical or diagonal 
        and calls the right routines.
        """
        if array[0, 0] == array[1, 0]:
            self.mark_straight_vent(array, horizontal=True)
        elif array[0, 1] == array[1, 1]:
            self.mark_straight_vent(array, horizontal=False)
        else:
            self.mark_diagonal_vent(array)

    def mark_straight_vent(self, array, horizontal=True):
        """
        Mark straight ventlines

        Parameters
        ----------
        array : np.array
            x1 y1
            x2 y2 
        horizontal : bool, optional
            whether or not it's horizontal or vertical, by default True
        """

        # Somethings wrong here!
        if horizontal:
            xmax, xmin = np.sort(array[:, 1])
            self.map[array[0, 0], xmin : xmax + 1] += 1

        if not horizontal:
            ymax, ymin = np.sort(array[:, 0])
            self.map[ymin : ymax + 1, array[1, 1]] += 1

    def mark_diagonal_vent(self, array):
        """
        Mark diagonal lines

        Parameters
        ----------
        array : [type]
            [description]
        """
        pass
