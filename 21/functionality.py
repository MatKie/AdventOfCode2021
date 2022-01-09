import copy
import numpy as np
from operator import mul
from functools import reduce


def deterministic_dice(start_1, start_2):
    Die = DeterministicDie()
    rolls = Die.roll()
    Player_1 = Player(start_1)
    Player_2 = Player(start_2)
    while not Player_2:
        x = next(rolls)
        Player_1.move_and_score(x)
        if Player_1:
            break
        Player_2.move_and_score(next(rolls))

    return Die.rolls * min(Player_1.score, Player_2.score)


class DeterministicDie(object):
    def __init__(self):
        self.rolls = 0

    def roll(self):
        while self.rolls < 1000:
            sum = 0
            for _ in range(3):
                self.rolls += 1
                sum += self.rolls
            yield sum


class Player(object):
    def __init__(self, starting_position, winning_score=1000):
        self.position = starting_position
        self.winning_score = winning_score
        self.score = 0

    def move_and_score(self, x):
        x += self.position
        self.position = x - (int(x / 10)) * 10
        if self.position == 0:
            self.position = 10
        self.score += self.position

    def __bool__(self):
        if self.score >= self.winning_score:
            return True

        return False


class DiracDice(object):
    def __init__(self, starting_position):
        self.starting_position = starting_position

    def find_all_universes(self):
        """DFS wrapper"""
        return self.depth_first_search(self.starting_position)

    @staticmethod
    def depth_first_search(
        position,
        score=0,
        universes=[],
        universes_increment=1,
        min_score=21,
        winning_universes=[],
    ):
        """
        DFS algorithm: Explore one path till you find end, then backtrack
        until there is a node with another possible way to go except 
        the backtracked way.
        Parameters
        ----------
        graph : dict
            bidirectional graph
        start : str
            current location in the graph
        end : str
            end node
        path : list, optional
            current path, by default []
        paths : list, optional
            all paths found so far, by default []
        Returns
        -------
        list (paths)
            all paths found
        """
        universes.append(universes_increment)
        if score >= min_score:
            winning_universes.append(reduce(mul, universes, 1))
            # winning_universes.append(np.prod(universes))

            # paths.append(path)
        else:
            # if there was start == target we backtrack (pop) items
            # from the path, until we reach a node with vertices
            # leading down other paths.
            # dead ends will be automatically popped as there are no
            # nodes at that graph[start].
            rolls = DiracDice.dice_roll()
            for position_increment, universes_increment in rolls:
                new_position = DiracDice.calc_position(position, position_increment)
                new_score = score + new_position
                DiracDice.depth_first_search(
                    new_position,
                    new_score,
                    universes,
                    universes_increment,
                    min_score,
                    winning_universes,
                )

        universes.pop()
        return winning_universes

    @staticmethod
    def dice_roll():
        return [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]

    @staticmethod
    def calc_position(position, position_increment):
        this_position = position + position_increment
        if this_position > 10:
            return this_position - 10
        else:
            return this_position
