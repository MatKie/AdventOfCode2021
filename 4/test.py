import pytest
import numpy as np
from functionality import BingoBoards, read_input


class TestInput:
    def test_read_input(self):
        """
        Make sure the matrices are read into the three dimensional
        array correctly
        """
        filename = "input.txt"
        drawn_numbers, matrices = read_input(filename)

        test_array = np.asarray(
            [
                [24, 53, 4, 8, 23],
                [0, 13, 48, 47, 83],
                [55, 56, 72, 50, 52],
                [82, 33, 58, 16, 11],
                [91, 7, 89, 9, 81],
            ]
        )

        zero_array = test_array - matrices[2, :, :]
        sum_zero = np.sum(np.abs(zero_array))

        assert sum_zero == pytest.approx(0)


class TestBingoBoards:
    def test_mark_boards(self):
        """
        Test the marking of boards.
        """
        # setup a three dimension test array
        test_number = 99
        d2_test_array = np.asarray(
            [
                [24, 53, 4, 8, 23],
                [99, 97, 97, 97, 99],
                [55, 56, 72, 50, 52],
                [82, 33, 58, 16, 11],
                [91, 7, 89, 9, 99],
            ]
        )
        d2_test_array_2 = np.copy(d2_test_array)
        d2_test_array_2[3, 2] = test_number
        d2_test_array_2[3, 3] = test_number
        d3_test_array = np.concatenate(([d2_test_array], [d2_test_array_2]))

        # Initialise BingBoard
        BingoBoard = BingoBoards(d3_test_array)

        # First mark not completing
        BingoBoard.mark_boards(test_number)
        boolean = BingoBoard.check_boards()
        assert boolean == False

        # Second Mark completing
        BingoBoard.mark_boards(97)
        boolean = BingoBoard.check_boards()
        assert boolean == True

