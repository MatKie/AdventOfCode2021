from os import read
from functionality import process_instruction, read_input, merge, count_blocks
import numpy as np


class TestInput:
    def test_read_input(self):
        instr = read_input("exampleinput.txt")

        assert len(instr) == 4
        assert instr[1][0] == "on"
        assert instr[2][0] == "off"
        assert instr[0][2] == (10, 12)


class TestProcessInstr:
    def test_instr(self):
        instr = read_input("exampleinput.txt")
        A = np.zeros((101, 101, 101), dtype=bool)
        A = process_instruction(A, instr[0])

        assert np.where(A == True)[0].shape[0] == 27

        for instruction in instr[1:]:
            A = process_instruction(A, instruction)

        assert np.where(A == True)[0].shape[0] == 39


class TestPart2:
    def test_example(self):
        new_blocks = read_input("exampleinput.txt")

        blocks = [new_blocks[0]]
        new_blocks = new_blocks[1:]

        while len(new_blocks) > 0:
            blocks, new_blocks = merge(blocks, new_blocks)
            print(count_blocks(blocks))

        assert count_blocks(blocks) == 39

    def test_part_1(self):
        new_blocks = read_input("exampleinput_1.txt")
        blocks = [new_blocks[0]]
        new_blocks = new_blocks[1:]

        while len(new_blocks) > 0:
            blocks, new_blocks = merge(blocks, new_blocks)

        print(count_blocks(blocks) / 590784)
        assert count_blocks(blocks) == 590784

    def test_part_2(self):
        new_blocks = read_input("exampleinput_2.txt")
        blocks = [new_blocks[0]]
        new_blocks = new_blocks[1:]

        i = 0
        while len(new_blocks) > 0:
            blocks, new_blocks = merge(blocks, new_blocks)
            i += 1

        print(count_blocks(blocks) / 2758514936282235)
        assert count_blocks(blocks) == 2758514936282235


# TestPart2().test_part_2()
