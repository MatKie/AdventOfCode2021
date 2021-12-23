import numpy as np
import pytest
from functionality import PathFinder, read_input, transform_input


class TestInput:
    def test_read_input(self):
        A = read_input("exampleinput.txt")

        assert A.shape == (10, 10)
        assert A[0, 0] == 1
        assert A[1, 1] == 3

    def test_transform_input(self):
        A = read_input("exampleinput.txt")
        A = transform_input(A)

        assert A.shape == (50, 50)
        assert A[0, 0] == 1
        assert A[10, 10] == 3
        assert A[40, 40] == 9
        assert A[3, 2] == 9
        assert A[13, 12] == 2


class TestPathfinder(object):
    def test_init_nodes(self):
        A = read_input("exampleinput.txt")

        ThisPath = PathFinder(A)
        nodes = ThisPath.get_initial_nodes()

        assert len(nodes) == 100
        assert nodes[(5, 5)] == [False, np.infty]

    def test_neighbour_nodes(self):
        A = read_input("exampleinput.txt")

        ThisPath = PathFinder(A)
        nodes = ThisPath.find_neighbours((0, 0))
        assert set(nodes) == set([(0, 1), (1, 0)])

        nodes = ThisPath.find_neighbours((5, 5))
        assert set(nodes) == set([(5, 4), (5, 6), (4, 5), (6, 5)])

        nodes = ThisPath.find_neighbours((9, 0))
        assert set(nodes) == set([(8, 0), (9, 1)])

        nodes = ThisPath.find_neighbours((0, 9))
        assert set(nodes) == set([(0, 8), (1, 9)])

    def test_algo(self):
        A = read_input("exampleinput.txt")
        ThisPath = PathFinder(A)

        total_cost = ThisPath.dijkstra_algo()

        assert total_cost == 40

    def test_algo_alt(self):
        A = read_input("exampleinput2.txt")
        ThisPath = PathFinder(A)

        total_cost = ThisPath.dijkstra_algo()

        assert total_cost == 8

    def test_algo2(self):
        A = read_input("exampleinput.txt")
        A = transform_input(A)
        ThisPath = PathFinder(A)

        total_cost = ThisPath.dijkstra_algo()

        assert total_cost == 315

