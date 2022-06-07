import pytest
from functionality import Node


class TestReadInput:
    def test_from_file(self):
        StartNode = Node.from_file("exampleinput.txt")

        assert StartNode.gallery == [0] * 11
        assert StartNode.rooms[2] == [100, 10]

    def test_hash(self):
        StartNode = Node.from_file("exampleinput.txt")

        with open("exampleinput.txt", "r") as f:
            string = f.readline()

        assert StartNode.hash() == string

    def test_hash_2(self):
        StartNode = Node.from_file("exampleinput.txt")
        StartNode.gallery[2] = 100

        with open("exampleinput.txt", "r") as f:
            string = f.readline()

        new_string = string[:2] + "C" + string[3:]

        assert StartNode.hash() == new_string


class TestMoves:
    def test_gallery(self):
        StartNode = Node.from_file("move_gallery.txt")

        (FN1, cost1), (FN2, cost2) = StartNode._move_gallery()
        assert FN1.rooms[2] == [0, 100]
        assert cost1 == 800
        assert FN2.rooms[2] == [0, 100]
        assert cost2 == 600

        ((FN3, cost3),) = FN1._move_gallery()
        assert FN3.rooms[2] == [100, 100]
        assert cost3 == cost2 - 100

