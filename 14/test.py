from os import read
import pytest
from functionality import read_input, Polymer, Polymeriser, SmartPolymer


class TestInput:
    def test_input(self):
        start, rules = read_input("exampleinput.txt")

        assert start == ["N", "N", "C", "B"]
        assert len(rules) == 16
        assert rules.get("BH") == "H"


class TestPolymer:
    def test_input(self):
        start, rules = read_input("exampleinput.txt")

        ThisPolymer = Polymer(start)

        assert ThisPolymer.pairs[0] == "NN"
        assert ThisPolymer.pairs[1] == "NC"
        assert ThisPolymer.pairs[2] == "CB"
        assert ThisPolymer.string_representation == "NNCB"

    def test_polymer_count(self):
        start, rules = read_input("exampleinput.txt")
        ThisPolymer = Polymer(start)

        ThisPolymeriser = Polymeriser(rules)
        for _ in range(10):
            ThisPolymer = ThisPolymeriser.polymerise(ThisPolymer)

        assert ThisPolymer.count_items() == 1588


class TestSmartPolymer:
    def test_input(self):
        start, rules = read_input("exampleinput.txt")

        ThisPolymer = SmartPolymer(start, rules)

        assert ThisPolymer.pair_counts["NN"] == 1
        assert ThisPolymer.pair_counts["NC"] == 1

    def test_polymer_count(self):
        start, rules = read_input("exampleinput.txt")
        ThisPolymer = SmartPolymer(start, rules)

        ThisPolymeriser = Polymeriser(rules)
        for _ in range(10):
            ThisPolymer = ThisPolymeriser.polymerise_smarter(ThisPolymer)

        assert ThisPolymer.count_items() == 1588


class TestPolymeriser:
    def test_polymerise(self):
        start, rules = read_input("exampleinput.txt")
        ThisPolymer = SmartPolymer(start, rules)

        ThisPolymeriser = Polymeriser(rules)
        ThisPolymer = ThisPolymeriser.polymerise_smarter(ThisPolymer)

        assert ThisPolymer.pair_counts["NC"] == 1
        assert ThisPolymer.pair_counts["CN"] == 1
        assert ThisPolymer.pair_counts["NB"] == 1
        assert ThisPolymer.pair_counts["BC"] == 1
        assert ThisPolymer.pair_counts["CH"] == 1
        assert ThisPolymer.pair_counts["HB"] == 1
        assert ThisPolymer.pair_counts["NN"] == 0
