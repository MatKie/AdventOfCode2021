from os import read
import numpy as np
import pytest
from functionality import Scanner, read_input, Map


class TestInput:
    def test_read_input(self):
        scanner_list = read_input("exampleinput.txt")

        assert len(scanner_list) == 2
        print(scanner_list)
        assert scanner_list[0][1] == (4, 1)


class TestOverlap:
    def test_2d_overlap(self):
        scanner_list = read_input("exampleinput.txt")

        Scanner0 = Scanner(scanner_list[0])
        Scanner1 = Scanner(scanner_list[1])

        ThisMap = Map(Scanner0)
        ThisMap.min_overlap = 3
        overlap = ThisMap.check_overlap(Scanner1)

        assert bool(overlap) == True
        assert overlap == (5, 2)


class TestRotation:
    def test_given_rotations(self):
        scanner_list = read_input("exampleinput_2.txt")

        Scanners = [Scanner(this_scanner) for this_scanner in scanner_list]

        count = 0
        for rotation in Scanners[0].rotations():
            for scanner in Scanners[1:]:
                scanner_set = set(tuple(row) for row in scanner.beacons)
                rotation_set = set(
                    tuple([int(r) for r in row]) for row in rotation.beacons
                )
                if scanner_set == rotation_set:
                    count += 1

        assert count == 4


class TestAddition:
    def test_number(self):
        scanner_list = read_input("exampleinput_3.txt")
        Scanners = [Scanner(this_scanner) for this_scanner in scanner_list]

        ThisMap = Map(Scanners[0])

        not_added = [i for i in range(1, len(Scanners))]
        j = 0
        while len(not_added) > 0 and j < 100:
            while_added = []
            for i, ThatScanner in enumerate(Scanners):
                if i in not_added:
                    success = ThisMap.add(ThatScanner)
                else:
                    success = True
                if not success:
                    while_added.append(i)
            not_added = while_added
            j += 1

        assert len(ThisMap) == 79

        with open("control_beacons.txt") as f:
            control_set = set()
            for line in f:
                line = tuple(int(i) for i in line.rstrip().split(","))
                control_set.add(line)

        assert control_set == ThisMap.beacon_set

    def test_sensor_distance(self):
        scanner_list = read_input("exampleinput_3.txt")
        Scanners = [Scanner(this_scanner) for this_scanner in scanner_list]

        ThisMap = Map(Scanners[0])

        not_added = [i for i in range(1, len(Scanners))]
        j = 0
        while len(not_added) > 0 and j < 100:
            while_added = []
            for i, ThatScanner in enumerate(Scanners):
                if i in not_added:
                    success = ThisMap.add(ThatScanner)
                else:
                    success = True
                if not success:
                    while_added.append(i)
            not_added = while_added
            j += 1

        maxdist = ThisMap.max_sensor_distance()

        assert maxdist == 3621


# TestAddition().test_number()
