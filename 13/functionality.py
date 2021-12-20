import numpy as np


class Folder(object):
    def __init__(self, filename):
        """
        Reads in an initial sheet of transparent paper and the folding
        instructions. Can fold it and visualise it. 

        Parameters
        ----------
        filename : str
            path to input
        """
        self.tuples, self.folds = self.read_input(filename)
        self.map = None
        self.n_rows, self.n_cols = 0, 0
        self.max_folds = len(self.folds)
        self.dots = None

    def transform_matrix(self):
        """
        Transforms a folded matrix to dots and hashes, writes it to output.txt
        """
        self.hash_matrix = np.empty((int(self.n_rows), int(self.n_cols)), dtype=str)
        self.hash_matrix[:, :] = "."
        self.hash_matrix[np.where(self.map > 0)] = "#"

        with open("output.txt", "w") as f:
            for row in range(int(self.n_rows)):
                string = self.hash_matrix[row, 0]
                for item in self.hash_matrix[row, 1:]:
                    string += item
                string += "\n"
                f.write(string)

    def fold(self):
        """
        Fold the transparent paper according to the next folding instruction
        initially read from the input.
        """
        direction, position = self.folds.pop(0)

        if direction == "y":
            self.map[:position, :] += self.map[-1:position:-1, :]
            self.map = self.map[:position, :]
            self.n_rows = (self.n_rows - 1) / 2
        else:
            self.map[:, :position] += self.map[:, -1:position:-1]
            self.map = self.map[:, :position]
            self.n_cols = (self.n_cols - 1) / 2

    def count_dots(self):
        """
        Count how many dots there are.
        """
        self.dots = np.where(self.map > 0)[0].shape[0]

    def construct_matrix(self):
        '''
        Check what the matrix dimension must be and and add a one to 
        dotted positions (instead of hash).
        '''
        for col, row in self.tuples:
            if row > self.n_rows:
                self.n_rows = row
            if col > self.n_cols:
                self.n_cols = col
        self.n_cols += 1
        self.n_rows += 1
        self.map = np.zeros((self.n_rows, self.n_cols))
        for col, row in self.tuples:
            self.map[row, col] = 1

    def read_input(self, filename):
        """
        Reads the input which consists out of dot positions (first part)
        and folding instruction (second part)

        Parameters
        ----------
        filename : str
            filepath

        Returns
        -------
        two lists
            firstly a list of tuples of dot location (x, y) -> (col, row) 
            and then a list of tuples of folds ('y'/'x', position).
        """
        tuples = []
        folds = []

        with open(filename, "r") as f:
            read_part_1 = True
            while read_part_1:
                line = f.readline().rstrip()
                if line == "":
                    read_part_1 = False
                    continue
                tuples.append(tuple(int(item) for item in line.split(",")))

            for line in f:
                line = line.rstrip()
                direction, position = line.split()[-1].split("=")
                folds.append((direction, int(position)))

        return tuples, folds
