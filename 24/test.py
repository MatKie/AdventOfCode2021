from dis import Instruction
import pytest
from functionality import solve_alu, read_instructions, ALU


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


class TestProduction:
    def test_last_instruction(self):
        # This yields zero for the last set of instructions
        _instructions = read_instructions("input.txt")
        instructions = ["inp z 9"] + _instructions[-18:]

        Alu = ALU()
        Alu = solve_alu(Alu, instructions, "7")

        assert Alu.states.get("z") == 0


class TestFirstInstructions:
    def test_one_two(self):
        _instructions = read_instructions("input.txt")
        instructions = _instructions[:18]

        all_states = [
            [i, j, k, l]
            for i in range(1, 10)
            for j in range(1, 10)
            for k in range(1, 10)
            for l in range(1, 10)
        ]
        with open("output.txt", "w") as f:
            for states in all_states:
                Alu = ALU()
                for k, i in enumerate(states):
                    instructions = _instructions[k * 18 : (k + 1) * 18]
                    Alu = solve_alu(Alu, instructions, "{:d}".format(i))

                f.write("z: {:d}".format(Alu.states.get("z")))
                f.write(", states: {:d}, {:d}, {:d}, {:d}".format(*states))
                f.write("\n")

        assert 0 == 1

    def test_all(self):
        _instructions = read_instructions("input.txt")
        instructions = _instructions[:18]
        z0 = 1
        z = []
        Alu = ALU()
        for k, i in enumerate([2, 9, 9, 9, 1, 9, 9, 3, 6, 9, 8, 4, 6, 9]):
            # Alu = solve_alu(Alu, instructions, "{:d}".format(1))
            instructions = _instructions[k * 18 : (k + 1) * 18]
            # print(Alu.states)
            Alu = solve_alu(Alu, instructions, "{:d}".format(i))

            print(k + 1, Alu.states, Alu.states.get("z") / z0, Alu.states.get("z") % 26)
            z0 = Alu.states.get("z")
            z.append(Alu.states.get("z"))

        assert 0 == 1


# TestFirstInstructions().test_one_two()
