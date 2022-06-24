# I might have to use memoization somehow..
# There are 8^14 ~= 4.4e12 SN to go through,
# Currently I recalculate the instructions for the first few letters
# all the time, however if I don't do that but save them, each number will
# be much quicker to calculate. Should be a 13/14 increase for the lowest
# digits in the SN and then increasingly inefficient as it goes to the higher
# digits in the SN. Worth it?
import copy

# Might run into a space problem, won't we.
class ALU(object):
    """
    Arithmetic logic unit

    Takes the instructions and keeps track of the states
    of variables
    """

    def __init__(self):
        self.states = {"x": 0, "y": 0, "z": 0, "w": 0}
        self.valid = True
        self.methods = {
            "add": self._add,
            "mul": self._multiply,
            "div": self._floor_divide,
            "mod": self._mod,
            "eql": self._equal,
            "inp": self._input,
        }

    def do_instruction(self, method, var, value):
        value = self.states.get(value) if value in self.states else int(value)
        self.states[var] = self.methods.get(method)(self.states[var], value)

    def _input(self, _old_var, value):
        return value

    def _equal(self, val1, val2):
        if val1 == val2:
            return 1
        return 0

    def _add(self, val1, val2):
        return val1 + val2

    def _multiply(self, val1, val2):
        return val1 * val2

    def _floor_divide(self, val1, val2):
        if val2 != 0:
            return val1 // val2
        else:
            self.valid = False

    def _mod(self, val1, val2):
        if val1 >= 0 and val2 > 0:
            return val1 % val2
        else:
            self.valid = False


def read_instructions(filename):
    instructions = []
    with open(filename, "r") as f:
        for line in f:
            instructions.append(line.strip("\n"))
    return instructions


def find_highest_monad(instructions):
    desired_z = 0
    instruction_counter = 13
    sn = ""
    for instruction_counter in range(13, -1, -1):
        for w in range(9, 0, -1):
            for z_prior in range(260000):
                Alu = ALU()
                current_instructions = ["inp z {:d}".format(z_prior)]
                current_instructions.extend(
                    instructions[
                        instruction_counter * 18 : (instruction_counter + 1) * 18
                    ]
                )
                Alu = solve_alu(Alu, current_instructions, w)
                if Alu.states.get("z") == desired_z and Alu.valid:
                    break
            if Alu.states.get("z") == desired_z and Alu.valid:
                desired_z = z_prior
                sn = str(w) + sn
                break
        print(sn, desired_z)

    return sn


def solve_alu(MonadAlu, instructions, sn_i):
    for instr in instructions:
        instr = instr.split()
        if len(instr) < 3:
            instr.append(sn_i)
        MonadAlu.do_instruction(*instr)

    return MonadAlu
