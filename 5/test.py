from os import read
import numpy as np
from numpy import testing
from functionality import read_input, find_xy_max, Map


class TestInput:
    def test_read_input(self):
        ventlines = read_input("exampleinput.txt")

        assert ventlines.shape[0] == 10

        assert ventlines[5, 1, 1] == 0

        assert type(ventlines[0, 0, 0] == np.int)


class TestXYMax:
    def test_xy_max(self):
        ventlines = read_input("exampleinput.txt")
        x_max, y_max = find_xy_max(ventlines)

        assert x_max == 10
        assert y_max == 10


class TestMap:
    def test_map_horizontal(self):
        ventlines = read_input("exampleinput.txt")
        x_max, y_max = find_xy_max(ventlines)
        TestMap = Map(x_max, y_max)

        for array in ventlines:
            TestMap.mark_vent(array)
            print(array)

        print(TestMap.map)

        assert 0 == 1


A = TestMap()
A.test_map_horizontal()
