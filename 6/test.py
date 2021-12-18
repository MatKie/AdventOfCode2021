import numpy as np

from functionality import Population, read_input, descendants_of_descendants


class TestPopulation:
    def test_18_days(self):
        initial_population = read_input("exampleinput.txt")

        FishPopulation = Population(initial_population)
        FishPopulation.propagate_population(18)
        assert FishPopulation.fish == 26

    def test_80_days(self):
        initial_population = read_input("exampleinput.txt")

        FishPopulation = Population(initial_population)
        FishPopulation.propagate_population(80)
        assert FishPopulation.fish == 5934


class TestRecursion:
    def test_18_days_recursion(self):
        initial_population = read_input("exampleinput.txt")
        # initial_population = [3]

        x = 0
        for xi in initial_population:
            x += descendants_of_descendants(80, xi)

        assert x == 100


TestRecursion().test_18_days_recursion()
