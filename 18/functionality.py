from numpy import ceil, floor
import re


def add(a, b):
    """
    Add two snail numbers a+b = [a,b]

    Parameters
    ----------
    a : str
    b : str

    Returns
    -------
    str
    """
    c = "[{:s},{:s}]".format(a, b)
    return c


def process_number(number, do_split=True, do_explode=True):
    """
    High level function to check when to do what. 

    Parameters
    ----------
    number : str
        snail number
    do_split : bool, optional
        for testing purposes, by default True
    do_explode : bool, optional
        for testing purposes, by default True

    Returns
    -------
    str
        snail number
    """
    exploded = explode(number)
    if exploded != number and do_explode:
        return process_number(exploded)
    else:
        splitd = split(number)
        if splitd != number and do_split:
            return process_number(splitd)
        else:
            return splitd


def explode(data):
    """
    Explode the string using regex. Search all regular number pairs [d,d],
    check the level by counting opening/closing brackets. 
    If not at least level four, look for the next pair.
    IF a level 5 pair is found explode it: 
        break string in left and right from pair
        find next number (if there is one)
        add left/right number to next number
        reconstruct string with that number there -- brackets 
        are taken care of by breaking string from pair
        add left and right with a zero inbetween 

    Parameters
    ----------
    data : str
        snail number in string representation

    Returns
    -------
    str
        snail number in string representation
    """
    offset = 0
    for p in re.findall("\[\d+,\d+\]", data):
        # Gives a regex search object with span and start. I think
        # gets rid of the brackets as well.
        pair = re.search(re.escape(p), data[offset:])
        left_brackets = data[: pair.start() + offset].count("[")
        right_brackets = data[: pair.start() + offset].count("]")
        if left_brackets - right_brackets >= 4:
            x, y = pair.group()[1:-1].split(",")
            # split the string into two parts at the pair
            # flip left side around so we get the first num going backwards
            left = data[: pair.start() + offset][::-1]
            right = data[pair.end() + offset :]
            # look left for first number -- if there's none do nothing
            search_left = re.search("\d+", left)
            if search_left:
                # need to find the rightmost match not the first (first since
                # we reversed the string)
                amt = int(left[search_left.start() : search_left.end()][::-1]) + int(x)
                # Write string backwards -- leave out bit betwen start() and end()
                left = f"{left[:search_left.start()]}{str(amt)[::-1]}{left[search_left.end():]}"
            # look right for first number -- if there's none do nothing
            search_right = re.search("\d+", right)
            if search_right:
                # Same procedure but string wasn't flipped
                amt = int(right[search_right.start() : search_right.end()]) + int(y)
                right = (
                    f"{right[:search_right.start()]}{amt}{right[search_right.end():]}"
                )
            # One of the ends will always be a zero, since snailfish numberes
            # are pairs and therefore one won't have a direct neighbour.
            data = f"{left[::-1]}0{right}"
            break
        else:
            # I don't know what it's here for but it makes some tests pass
            offset = pair.end() + offset
            pass
    return data


def split(data):
    """
    Split numbers > 9

    Parameters
    ----------
    data : str
        snailnumber

    Returns
    -------
    str
        snailnumber
    """
    dd = re.search("\d\d", data)
    if dd:
        left = data[: dd.start()]
        right = data[dd.end() :]
        left_digit = int(floor(int(dd.group()) / 2))
        right_digit = int(ceil(int(dd.group()) / 2))
        data = f"{left}[{left_digit},{right_digit}]{right}"
    return data


def magnitude(data):
    """
    Calculates the magnitude of a snail number. It goes over all
    pairs of [d1,d2] and reduces them to 3*d1 + 2*d2, which will reduce
    the nesting and create a new pair to be evaluated until there is 
    only one pair (the final magnitude)

    Parameters
    ----------
    data : str
        snailnumber

    Returns
    -------
    int
        magnitude
    """
    while data.count(",") > 1:
        for p in re.findall("\[\d+,\d+\]", data):
            pair = re.search(re.escape(p), data)
            left_digit, right_digit = p[1:-1].split(",")
            data = f"{data[: pair.start()]}{int(left_digit) * 3 + int(right_digit) * 2}{data[pair.end() :]}"
    left_digit, right_digit = data[1:-1].split(",")
    return int(left_digit) * 3 + int(right_digit) * 2
