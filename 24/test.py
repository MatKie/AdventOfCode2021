from dis import Instruction
import pytest
from functionality import read_instructions, monad, find_highest_monad, ALU


class TestInput:
    def test_read_instr(self):
        instructions = read_instructions("exampleinput_2.txt")

        assert instructions[1] == "inp x"
        assert instructions[-1] == "eql z x"


class TestALU:
    def test_inp(self):
        Alu = ALU()
        Alu.do_instruction("inp", "x", "5")
        assert Alu.states.get("x") == 5

    def test_add(self):
        Alu = ALU()
        Alu.do_instruction("inp", "x", "5")
        Alu.do_instruction("inp", "y", "2")
        Alu.do_instruction("add", "x", "y")
        assert Alu.states.get("x") == 7

    def test_mul(self):
        Alu = ALU()
        Alu.do_instruction("inp", "x", "5")
        Alu.do_instruction("inp", "y", "2")
        Alu.do_instruction("mul", "x", "y")
        assert Alu.states.get("x") == 10

    def test_div(self):
        Alu = ALU()
        Alu.do_instruction("inp", "x", "5")
        Alu.do_instruction("inp", "y", "2")
        Alu.do_instruction("div", "x", "y")
        assert Alu.states.get("x") == 2

    def test_div(self):
        Alu = ALU()
        Alu.do_instruction("inp", "x", "5")
        Alu.do_instruction("inp", "y", "2")
        Alu.do_instruction("mod", "x", "y")
        assert Alu.states.get("x") == 1

    def test_eql_1(self):
        Alu = ALU()
        Alu.do_instruction("inp", "x", "5")
        Alu.do_instruction("inp", "y", "2")
        Alu.do_instruction("eql", "x", "y")
        assert Alu.states.get("x") == 0

    def test_eql_2(self):
        Alu = ALU()
        Alu.do_instruction("inp", "x", "5")
        Alu.do_instruction("inp", "y", "5")
        Alu.do_instruction("eql", "x", "y")
        assert Alu.states.get("x") == 1


class TestMonad:
    def test_example_1(self):
        instructions = read_instructions("exampleinput_2.txt")

        assert monad("39", instructions) == True
        assert monad("38", instructions) == False

