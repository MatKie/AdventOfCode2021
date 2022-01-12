def read_input(filename):
    instr = []
    with open(filename, "r") as f:
        for line in f:
            split_line = line.strip().split(",")
            state, split_line[0] = split_line[0].split()
            coords = [item.split("..") for item in split_line]
            coords = [(int(min[2:]), int(max)) for min, max in coords]
            instr.append([state, *coords])

    return instr


def process_instruction(A, instruction):
    state = False
    if instruction[0] == "on":
        state = True

    x, y, z = instruction[1:]
    if True in [True if min < -50 or max > 50 else False for (min, max) in [x, y, z]]:
        return A
    for xi in range(x[0] + 50, x[1] + 51):
        for yi in range(y[0] + 50, y[1] + 51):
            for zi in range(z[0] + 50, z[1] + 51):
                A[xi, yi, zi] = state

    return A


def check_overlap(block, new_block):
    # Need to overlap / be enclosed in all three dimensions (need be three)
    overlap = 0
    enclosed = 0
    for coords, new_coords in zip(block[1:], new_block[1:]):
        c1, c2 = coords
        nc1, nc2 = new_coords
        if nc1 >= c1 and nc2 <= c2:
            enclosed += 1
            overlap += 1
        elif (nc1 >= c1 and nc1 <= c2) or (nc2 <= c2 and nc2 >= c1):
            overlap += 1

    return overlap, enclosed


def split(block, new_block):
    split_blocks = []
    # Only called on overlapping blocks
    xmin, xmax = block[1]
    ymin, ymax = block[2]
    zmin, zmax = block[3]

    new_block_state = new_block[0]
    nxmin, nxmax = new_block[1]
    nymin, nymax = new_block[2]
    nzmin, nzmax = new_block[3]

    if nxmin < xmin:
        split_blocks.append(
            [new_block_state, (nxmin, xmin - 1), (nymin, nymax), (nzmin, nzmax)]
        )
        nxmin = xmin
    if nxmax > xmax:
        split_blocks.append(
            [new_block_state, (xmax + 1, nxmax), (nymin, nymax), (nzmin, nzmax)]
        )
        nxmax = xmax

    if nymin < ymin:
        split_blocks.append(
            [new_block_state, (nxmin, nxmax), (nymin, ymin - 1), (nzmin, nzmax)]
        )
        nymin = ymin
    if nymax > ymax:
        split_blocks.append(
            [new_block_state, (nxmin, nxmax), (ymax + 1, nymax), (nzmin, nzmax)]
        )
        nymax = ymax

    if nzmin < zmin:
        split_blocks.append(
            [new_block_state, (nxmin, nxmax), (nymin, nymax), (nzmin, zmin - 1)]
        )
        nzmin = zmin
    if nzmax > zmax:
        split_blocks.append(
            [new_block_state, (nxmin, nxmax), (nymin, nymax), (zmax + 1, nzmax)]
        )
        nzmax = zmax

    return split_blocks


def merge(blocks, new_blocks):
    for i_nb, bn in enumerate(new_blocks):
        for j_b, b in enumerate(blocks):
            overlap, enclosed = check_overlap(b, bn)
            new_state = bn[0]
            if overlap == 3 and new_state == "off":
                # Split original block in (up to) six parts
                split_blocks = split(bn, b)
                return (
                    blocks[:j_b] + split_blocks + blocks[j_b + 1 :],
                    new_blocks[:i_nb] + new_blocks[i_nb + 1 :],
                )
            if overlap == 3 and new_state == "on":
                split_blocks = split(b, bn)
                return blocks, new_blocks[:i_nb] + split_blocks + new_blocks[i_nb + 1 :]
            if overlap < 3 and new_state == "off":
                return blocks, new_blocks[:i_nb] + new_blocks[i_nb + 1 :]
            if overlap < 3 and new_state == "on":
                return blocks + [bn], new_blocks[:i_nb] + new_blocks[i_nb + 1 :]

    return blocks, new_blocks


def count_blocks(blocks):
    sum = 0
    for block in blocks:
        product = 1
        for cmin, cmax in block[1:]:
            product *= cmax + 1 - cmin
        sum += product
    return sum
