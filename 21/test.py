from functionality import deterministic_dice, DiracDice
import pytest
import numpy as np


class TestExample:
    def test_full(self):
        output = deterministic_dice(4, 8)

        assert output == 739785


class TestDirac:
    def test_start_one(self):
        Dice = DiracDice(4)
        universes = Dice.find_all_universes()
        this_sum = sum(universes)
        print(this_sum)

        assert this_sum == 444356092776315

    def test_start_two(self):
        Dice = DiracDice(8)
        universes = Dice.find_all_universes()
        this_sum = sum(universes)
        print(this_sum)

        assert this_sum == 341960390180808


# TestDirac().test_start_one()
