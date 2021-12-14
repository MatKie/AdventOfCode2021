import pytest
from numpy import ndarray
from functionality import find_cost, read_input, find_optimal_position
from functionality import find_cost_p2, find_optimal_position_p2


class TestExample:
    def test_input(self):
        input_vector = read_input("exampleinput.txt")

        assert type(input_vector) == ndarray
        assert input_vector.shape == (10,)

    def test_cost(self):
        input_vector = read_input("exampleinput.txt")

        cost = find_cost(input_vector, 3)
        assert cost == 39

        cost = find_cost(input_vector, 2)
        assert cost == 37

    def test_find_optimal_cost(self):
        input_vector = read_input("exampleinput.txt")

        position = find_optimal_position(input_vector)

        assert position == 2


class TestExampleP2:
    def test_cost(self):
        input_vector = read_input("exampleinput.txt")

        cost = find_cost_p2(input_vector, 2)
        assert cost == 206

        cost = find_cost_p2(input_vector, 5)
        assert cost == 168

    def test_find_optimal_cost(self):
        input_vector = read_input("exampleinput.txt")
        position = find_optimal_position_p2(input_vector)

        assert position == 5

