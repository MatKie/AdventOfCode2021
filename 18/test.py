import pytest
from functionality import process_number


class TestSplit(object):
    def test_split_1(self):
        number = "[[[[0,7],4],[15,[0,13]]],[1,1]]"
        number = process_number(number, do_explode=False)

        assert number == "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]"


class TestExplode(object):
    def test_explode_1(self):
        number = "[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]"
        number = process_number(number, do_explode=True)

        assert number == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"

    def test_explode_2(self):
        number = "[[6,[5,[4,[3,2]]]],1]"
        number = process_number(number, do_explode=True)

        assert number == "[[6,[5,[7,0]]],3]"

    def test_explode_3(self):
        number = "[[[[[9,8],1],2],3],4]"
        number = process_number(number)

        assert number == "[[[[0,9],2],3],4]"


# TestExplode().test_explode_1()
