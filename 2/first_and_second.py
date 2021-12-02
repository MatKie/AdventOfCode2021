import numpy as np

horizontal, vertical = 0, 0
# whenever it's forward add x to horizontal
# whenever it's up subtract x to vertical
# whenever it's down add x to vertical
with open('input.txt', 'r') as f:
    for line in f:
        this_line = line.rstrip()
        direction, x = this_line.split(' ')
        x = int(x)
        if direction == 'forward':
            horizontal = horizontal + x
            continue
        if direction == 'up':
            vertical -= x
        else:
            vertical += x
print(f'Vertical position: {vertical}')
print(f'Horizontal position: {horizontal}')
print(f'Product: {vertical*horizontal}')

horizontal, vertical, aim = 0, 0, 0
# whenever it's forward add x to horizontal, mutliply aim by x and add to
# vertical.
# whenever it's up subtract x to aim
# whenever it's down add x to aim
with open('input.txt', 'r') as f:
    for line in f:
        this_line = line.rstrip()
        direction, x = this_line.split(' ')
        x = int(x)
        if direction == 'forward':
            horizontal = horizontal + x
            vertical += aim * x
            continue
        if direction == 'up':
            aim -= x
        else:
            aim += x
print(f'Vertical position: {vertical}')
print(f'Horizontal position: {horizontal}')
print(f'Product: {vertical*horizontal}')






