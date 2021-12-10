import numpy as np


def read_input(filename, n_matrices=100):
    """
    Read first line of filename as drawn numbers and then 
    read the 5x5 matrices afterwards until the end of the file.

    Assumes number of matrices is known when array is passed
    """
    with open(filename, "r") as f:
        drawn_numbers = f.readline()
        drawn_numbers = [int(item) for item in drawn_numbers.split(",")]

        matrices = np.zeros((n_matrices, 5, 5))
        # First read line is an empty line which ups the counter
        third_dimension = -1
        n_row = 0
        for line in f:
            if line == "\n":
                third_dimension += 1
                n_row = 0
                continue
            line = line.rstrip().split()
            vector = np.array(line, dtype=np.uint32)
            matrices[third_dimension, n_row, :] = vector
            n_row += 1

        return drawn_numbers, matrices


class BingoBoards(object):
    def __init__(self, matrices):
        """
        Holds the original matrices and 'crosses off' the called 
        numbers.

        Crossing off is done by assigning a -1 to the respective position.

        Parameters
        ----------
        matrices : array like
            three dimension array of 5x5 matrices. 
        """
        self.matrices = matrices

    def mark_boards(self, drawn_number):
        """
        This method assigns a -1 to every position on every board where
        drawn number appears

        Parameters
        ----------
        drawn_number : int
            positive integer
        """
        self.matrices = np.where(self.matrices == drawn_number, -1, self.matrices)

    def check_boards(self):
        """
        This method checks if a row or column of any board is zero. 
        """
        where_output = np.where(self.matrices == -1)

        return False
