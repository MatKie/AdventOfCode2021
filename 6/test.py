import numpy as np

from functionality import Population, read_input


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
