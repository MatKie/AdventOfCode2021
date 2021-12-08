import numpy as np
import pytest
from classes_functions import BinaryArray, BinaryConverter, invert
from classes_functions import find_scrubber_number
def test():
    A = np.array([0,1,0,0,1])
    B = BinaryConverter(A)
    assert B.decimal == 9


def test_invert():
    B = invert(np.array([0,1,0,0,1]))
    C = BinaryConverter(B)
    assert C.decimal == 22

class TestSecondStar():
    def setup(self):
        self.A = [
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010'
            ]

    def test_binary_array(self):
        self.setup()
        BinArr = BinaryArray(self.A, do_invert=False)
        result3 = np.array([1, 0, 1, 1, 1])
        
        for i in range(5):
            assert BinArr.binary_array[3, i] == result3[i]

    def test_o2_rating(self):
        self.setup()
        BinArr = BinaryArray(self.A)
        
        scrubber = find_scrubber_number(BinArr) 

        result = np.array([1,0,1,1,1])
        
        for i in range(5):
            assert scrubber[i] == result[i]
    
    def test_co2_rating(self):
        self.setup()
        BinArr = BinaryArray(self.A, do_invert=True)

        scrubber = find_scrubber_number(BinArr) 

        result = np.array([0,1,0,1,0])
        
        for i in range(5):
            assert scrubber[i] == result[i]
oxygen_rating = BinaryConverter(oxygen_rating_binary).decimal
