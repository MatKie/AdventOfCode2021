    '''
    I wrote all the stuff on my own, but here are links for further/better
    solutions:
    https://www.reddit.com/r/adventofcode/comments/rmbp88/2021_day_22_how_to_think_about_the_problem/
    https://stackoverflow.com/questions/66135217/how-to-subdivide-set-of-overlapping-aabb-into-non-overlapping-set-of-aabbs
    https://www.youtube.com/watch?v=7gW_h0RTDd8
    https://www.youtube.com/watch?v=YKpViLcTp64
    '''
from functionality import read_input, process_instruction, merge, count_blocks
import numpy as np

instr = read_input("input.txt")
A = np.zeros((101, 101, 101), dtype=bool)

for instruction in instr[:-2]:
    A = process_instruction(A, instruction)

number_on = np.where(A == True)[0].shape[0]

print("***Part 1***")
print("Number of on segments: {:d}".format(int(number_on)))


new_blocks = read_input("input.txt")
blocks = [new_blocks[0]]
new_blocks = new_blocks[1:]
while len(new_blocks) > 0:
    blocks, new_blocks = merge(blocks, new_blocks)

print("***Part 3***")
print("Number of on segments: {:d}".format(int(count_blocks(blocks))))
