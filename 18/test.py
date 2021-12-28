import pytest
from functionality import process_number, add


class TestSplit(object):
    def test_combine(self):
        number = "[[[[0,7],4],[15,[0,13]]],[1,1]]"
        number = process_number(number, do_explode=True)

        assert number == "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"

    def test_addition(self):
        snail_numbers = []
        with open("exampleinput.txt", "r") as f:
            for line in f:
                snail_numbers.append(line.strip())

        addition = add(snail_numbers[0], snail_numbers[1])
        print(addition)
        result = process_number(addition)

        for snail_number in snail_numbers[2:]:
            addition = add(result, snail_number)
            result = process_number(addition)

        assert result == "[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]"


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

