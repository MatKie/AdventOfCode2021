import copy
import numpy as np
from operator import mul
from functools import reduce


def deterministic_dice(start_1, start_2):
    '''
    Plays a game of deterministic dice, given the starting
    position on the board
    '''
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
        '''
        A deterministic dice increasing it's result 
        by one at every roll, keeping track of how often it rolled.
        '''
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
        '''
        Player for deterministic dice, main method is the move method.
        '''
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


class DiracPlayer(object):
    def __init__(self, starting_position, winning_score=21):
        '''
        Dirac Dice player, mostly to keep track of past scores and it's winning 
        universes.
        '''
        self.positions = [starting_position]
        self.scores = [0]
        self.winning_universes = []
        self.winning_score = winning_score

    def __bool__(self):
        if sum(self.scores) >= self.winning_score:
            return True

        return False


class DiracDice(object):
    def __init__(self, starting_position_1, starting_position_2):
        self.starting_position = starting_position_1
        self.Player_1 = DiracPlayer(starting_position_1, 21)
        self.Player_2 = DiracPlayer(starting_position_2, 21)

    def find_all_universes(self):
        """DFS wrapper"""
        return self.depth_first_search(self.Player_1, self.Player_2)

    @staticmethod
    def depth_first_search(Player1, Player2, universes=[], universes_increment=1):
        """
        DFS algorithm: Explore one path till you find end, then backtrack
        until there is a node with another possible way to go except 
        the backtracked way.
        Parameters
        ----------
        Player1, Player2 : DiracPlayer objects
        universes : list
            List of how many universes the current path exists in (needs be 
            multiplied to yield this number).
        univereses_increment : int
            Keeps track of how many universes the last set of three
            dice rolls opened up. 
        Returns
        -------
        list of int 
            List of how many universes each player one in (needs be summed up)
        """
        universes.append(universes_increment)
        if Player1:
            Player1.winning_universes.append(reduce(mul, universes, 1))
        elif Player2:
            Player2.winning_universes.append(reduce(mul, universes, 1))
        else:
            rolls = DiracDice.dice_roll()
            for position_increment, universes_increment in rolls:
                # This is not necessary as we don't really need to keep
                # track of our Players, just switch them at each 
                # recursive call. However it was easier for me to figure
                # out that way.
                if (len(universes) % 2) == 0:
                    new_position = DiracDice.calc_position(
                        Player2.positions[-1], position_increment
                    )
                    Player2.positions.append(new_position)
                    Player2.scores.append(new_position)
                    Player1.scores.append(0)
                    Player1.positions.append(Player1.positions[-1])
                else:
                    new_position = DiracDice.calc_position(
                        Player1.positions[-1], position_increment
                    )
                    Player1.positions.append(new_position)
                    Player1.scores.append(new_position)
                    Player2.scores.append(0)
                    Player2.positions.append(Player2.positions[-1])
                DiracDice.depth_first_search(
                    Player1, Player2, universes, universes_increment
                )

        # BACKTRACK
        universes.pop()
        for Player in [Player1, Player2]:
            Player.scores.pop()
            Player.positions.pop()
        return Player1.winning_universes, Player2.winning_universes

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
