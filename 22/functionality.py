def read_input(filename):
    """
    Read input into blocks/instructions

    Parameters
    ----------
    filename : str
        path to filename

    Returns
    -------
    block
        [state, (xmin, xmax), (ymin, ymax), (zmin, zmax)]
    """
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
    """
    Brute force turn off/on elements in a matrix

    Parameters
    ----------
    A : np.ndarray
        block matrix
    instruction : block [state, (xmin, xmax)]
        a block to turn on or off dep. on state

    Returns
    -------
    np.ndarray
        matrix after processing an instruction
    """
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
    """
    Checks if the cubes overlap by comparing their  boudns
    """
    # Need to overlap / be enclosed in all three dimensions (need be three)
    overlap = 0
    for coords, new_coords in zip(block[1:], new_block[1:]):
        c1, c2 = coords
        nc1, nc2 = new_coords
        if (
            (nc1 >= c1 and nc1 <= c2)
            or (nc2 <= c2 and nc2 >= c1)
            or (nc1 < c1 and nc2 > c2)
            or (nc1 >= c1 and nc2 <= c2)
        ):
            overlap += 1

    return overlap


def split(block, new_block):
    """
    Split a new_block into parts not overlapping with block

    Parameters
    ----------
    block : a block ([state, (xmin,xmax), ...])
        Intended to stay complete
    new_block : a different block ([state, (xmin,xmax), ...])
        will be the split into the blocks not overlapping with block

    Returns
    -------
    a block ([state, (xmin, xmax)...])
        Up to six blocks which result from intersecting new_block with block.
    """
    split_blocks = []
    # Only called on overlapping blocks, no need to test
    xmin, xmax = block[1]
    ymin, ymax = block[2]
    zmin, zmax = block[3]

    new_block_state = new_block[0]
    nxmin, nxmax = new_block[1]
    nymin, nymax = new_block[2]
    nzmin, nzmax = new_block[3]

    # The -1 is necessary, to have non intersecting blocks after splitting.
    # A loop is totaly possible but I wanted to have it easy debugging.. also
    # it was hard to wrap my head around it
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
    """
    Merge the first member of new_blocks into blocks. If an overlap 
    is noticed, new_block will be split at the overlap and the function
    called again with the split pieces. 
    If new_block is an off block, the block overlapping will be split
    and we call the function again with the same new_blocks but 
    diff. blocks.

    Parameters
    ----------
    blocks : list of blocks/instructions
        see read_input
    new_blocks : list of blocks/instructions
        see read_input

    Returns
    -------
    blocks, new_blocks
        updated block list, see description
    """
    for i_nb, bn in enumerate(new_blocks):
        for j_b, b in enumerate(blocks):
            overlap = check_overlap(b, bn)
            new_state = bn[0]
            if overlap == 3 and new_state == "off":
                # Split original block in (up to) six parts
                split_blocks = split(bn, b)
                return (
                    blocks[:j_b] + split_blocks + blocks[j_b + 1 :],
                    new_blocks,
                )
            if overlap == 3 and new_state == "on":
                split_blocks = split(b, bn)
                return blocks, new_blocks[:i_nb] + split_blocks + new_blocks[i_nb + 1 :]

        if new_state == "off":
            return blocks, new_blocks[:i_nb] + new_blocks[i_nb + 1 :]
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
