import numpy as np


def read_input(filename):
    """
    Returns list of initial population

    Parameters
    ----------
    filename : string
        path to file

    Returns
    -------
    list of int
        initial states of the first fishes
    """
    with open(filename, "r") as f:
        initial_population = np.loadtxt(f, dtype=int, delimiter=",")

    return initial_population


class Population(object):
    def __init__(self, initial_population):
        """
        Class for representing a population of lantern fish of certain
        'maturity' and propagiting the population acc. to AoC day 6
        rules.
        """
        self.population = np.zeros((9))
        for i in initial_population:
            self.population[i] += 1

    @property
    def fish(self):
        """
        Number of fish in the population. We only keep track of how many
        fish are x days old in a list from 0 to 8 days.

        Returns
        -------
        int
        """
        return sum(self.population)

    def propagate_population(self, n_days):
        """
        Wrapper function to call propaget_one_day n_day times:

        propagates population by getting the number of reproducing fish
        (0 day maturity), then shifting all values one position to the
        left. The new fish are added to the last and seventh position in
        the population.
        """
        for _ in range(n_days):
            self.propagate_one_day()

    def propagate_one_day(self):
        """
        See propagate_population
        """
        new_fish = self.population[0]
        self.population[:-1] = self.population[1:]
        self.population[-1] = new_fish
        self.population[6] += new_fish


def descendants_of_descendants(n_days, initial_state):
    k = 0
    j = 1
    n = n_days
    i = initial_state

    d_of_d = current_descendants(n, i, j, k)
    fishes = 1

    while len(d_of_d) > 0:
        for l, ji in enumerate(d_of_d):
            k += 1
            new_d_of_d = current_descendants(n - (l * 7), i, ji, k)
            fishes += sum(d_of_d)
        d_of_d = new_d_of_d

    return fishes


def current_descendants(n, i, j, k):
    list_of_descendants = []
    for ji in range(j):
        descendants = (n - i - 9 * k - 7 * ji) / 7
        if descendants > 0:
            list_of_descendants.append(int(np.ceil(descendants)))

    return list_of_descendants
