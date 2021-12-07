import numpy as np
import pytest
from classes_functions import BinaryConverter, invert

def test():
    A = np.array([0,1,0,0,1])
    B = BinaryConverter(A)
    assert B.decimal == 9


def test_invert():
    B = invert(np.array([0,1,0,0,1]))
    C = BinaryConverter(B)
    assert C.decimal == 22