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
    valid = False
    sn = 100000000000000
    memoization = {}
    while not valid:
        sn -= 1
        string_sn = str(sn)
        if "0" not in string_sn:
            MonadAlu, memoization = do_instructions(
                memoization, string_sn, instructions
            )

            valid = not bool(MonadAlu.states.get("z"))
            # How to store non-finished ALUs? Recursion?
        if sn % 1e4 == 0:
            print(sn)
    return sn


def do_instructions(memoization, string_sn, instructions):
    for i in range(14, 0, -1):
        MonadAlu = memoization.get(string_sn[:i], None)
        if MonadAlu is not None:
            if i == 14:
                return MonadAlu, memoization
            memoization.update(
                {
                    string_sn[: i + 1]: get_this_alu(
                        copy.deepcopy(MonadAlu), instructions, i, string_sn[i]
                    )
                }
            )
            return do_instructions(memoization, string_sn, instructions)
        elif i == 1:
            memoization.update(
                {string_sn[:i]: get_this_alu(MonadAlu, instructions, 0, string_sn[0])}
            )
            return do_instructions(memoization, string_sn, instructions)


def get_this_alu(MonadAlu, instructions, start, sn_i):
    if MonadAlu is None:
        MonadAlu = ALU()
    j = -1
    if not MonadAlu.valid:
        return MonadAlu
    for instr in instructions:
        instr = instr.split()
        if len(instr) < 3:
            instr.append(sn_i)
            j += 1
        if j == start:
            MonadAlu.do_instruction(*instr)

    return MonadAlu
