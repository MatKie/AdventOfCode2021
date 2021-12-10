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
        self.n_matrices = matrices.shape[0]
        self.boards_of_interest = []
        self.bingoboard = None

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
        bingo = False
        where_output = np.where(self.matrices == -1)

        boards, rows, columns = where_output

        # Find which boards have more than four crossed out.
        unclear_matrices = [
            i for i in range(self.n_matrices) if i not in self.boards_of_interest
        ]
        for i in unclear_matrices:
            if len(np.where(boards == i)[0]) > 4:
                self.boards_of_interest.append(i)

        # Check if either rows or columns has five times the same number
        for n_board in self.boards_of_interest:
            if bingo:
                break
            positions = np.where(boards == n_board)
            for i in range(5):
                if len(np.where(rows[positions] == i)[0]) > 4:
                    bingo = True
                    self.bingoboard = n_board
                    break
                elif len(np.where(columns[positions] == i)[0]) > 4:
                    bingo = True
                    self.bingoboard = n_board
                    break

        return bingo

    def get_board_score(self):
        """
        Return the sum of the winning board, but only not crossed out fields.

        Returns
        -------
        int
            Board score
        """
        if self.bingoboard is not None:
            bingoboard = np.where(
                self.matrices[self.bingoboard] == -1, 0, self.matrices[self.bingoboard]
            )
            return np.sum(bingoboard)

        return None
