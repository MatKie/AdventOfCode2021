from dis import Instruction
from functionality import find_highest_monad, read_instructions

instructions = read_instructions("input.txt")
sn = find_highest_monad(instructions)

print("Highest possible SN:", sn)

