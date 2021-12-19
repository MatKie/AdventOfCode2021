import pytest
from functionality import read_input, OctopusMap
import numpy as np


class TestInput:
    def test_read_input(self):
        A = read_input("exampleinput.txt")

        assert A[2, 2] == 6
        assert A[2, 1] == 2


class TestOctopusMap:
    def test_step_1_3(self):
        A = read_input("exampleinput.txt")
        OctMap = OctopusMap(A)
        OctMap.step()

        S1 = read_input("step1.txt")
        assert np.sum(OctMap.power_levels - S1) == 0

        OctMap.step_to_n(2)
        S2 = read_input("step2.txt")
        print(OctMap.power_levels)
        assert np.sum(OctMap.power_levels - S2) == 0

    def test_step_10_100(self):
        A = read_input("exampleinput.txt")
        OctMap = OctopusMap(A)
        OctMap.step_to_n(10)

        S1 = read_input("step10.txt")
        assert np.sum(OctMap.power_levels - S1) == 0

        OctMap.step_to_n(100)
        S2 = read_input("step100.txt")
        print(OctMap.power_levels)
        assert np.sum(OctMap.power_levels - S2) == 0
        assert OctMap.n_flashes == 1656

    def test_synchronisation(self):
        A = read_input("exampleinput.txt")
        OctMap = OctopusMap(A)

        while not OctMap.synchronised or OctMap.n_step > 1000:
            OctMap.step()

        assert OctMap.synchronised == 195
