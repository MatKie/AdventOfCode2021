from functionality import read_input, process_instruction
import numpy as np

instr = read_input("input.txt")
A = np.zeros((101, 101, 101), dtype=bool)

for instruction in instr[:-2]:
    A = process_instruction(A, instruction)

number_on = np.where(A == True)[0].shape[0]

print("***Part 1***")
print("Number of on segments: {:d}".format(int(number_on)))
