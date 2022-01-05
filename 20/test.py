from os import read
from types import new_class
import pytest
from functionality import PictureEnhancer, read_input
import numpy as np


class TestInput:
    def test_read_input(self):
        code, picture = read_input("exampleinput.txt")

        assert type(code) == str
        assert len(code) == 512

        assert picture.shape == (5, 5)
        assert picture[2, 1] == 1
        assert picture[2, 2] == 0


class TestEnhancer:
    def test_enhance_picture(self):
        code, picture = read_input("exampleinput.txt")

        PE = PictureEnhancer(code)

        new_picture = PE.enhance_picture(picture, 0)

        assert np.sum(new_picture) == 24

        new_picture = PE.enhance_picture(new_picture, 1)

        assert np.sum(new_picture) == 35

    def test_padding(self):
        code, picture = read_input("exampleinput.txt")

        PE = PictureEnhancer(code)
        PE.padding = 10

        new_picture = PE.enhance_picture(picture, 0)

        assert np.sum(new_picture) == 24

    def test_padding_2(self):
        code, picture = read_input("input.txt")

        PE1 = PictureEnhancer(code)
        PE2 = PictureEnhancer(code)
        PE2.padding = 5

        p1 = PE1.enhance_picture(picture, 0)
        p1 = PE1.enhance_picture(p1, 1)
        p2 = PE2.enhance_picture(picture, 0)
        p2 = PE2.enhance_picture(p2, 1)

        assert np.sum(p1) == np.sum(p2)

    def test_ballpark(self):
        code, picture = read_input("input.txt")

        PE1 = PictureEnhancer(code)

        p1 = PE1.enhance_picture(picture, 0)
        p1 = PE1.enhance_picture(p1, 1)

        assert np.sum(p1) > 5543
        assert np.sum(p1) < 5971


