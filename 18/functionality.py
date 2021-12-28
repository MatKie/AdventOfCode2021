from numpy import ceil, floor
import re


def process_number(number, do_split=True, do_explode=True):
    level = 0
    new_number = ""
    skip = False
    for i, char in enumerate(number):
        if skip:
            skip = False
            continue
        if char == "[":
            level += 1
            new_number += char
            continue
        elif char == "]":
            level -= 1
            new_number += char
            continue
        elif char == ",":
            new_number += char
            continue
        else:
            if number[i + 1] in ["[", "]", ","]:
                this_number = int(char)
            else:
                skip = True
                this_number = int(number[i : i + 2])

        if level > 4 and do_explode:
            new_number = explode(number)
            level -= 1
            return process_number(new_number, do_split=do_split, do_explode=do_explode)
            # explode next pair

        if this_number > 10 and do_split:
            left, right = floor(this_number / 2.0), ceil(this_number / 2.0)
            new_number += "[{:d},{:d}]".format(int(left), int(right))
            new_number += number[i + 2 :]
            return process_number(new_number, do_split=do_split, do_explode=do_explode)
            # split this number

        new_number += str(this_number)
    return new_number


def explode(data):
    """
    Explode the string using regex. Search all regular number pairs [d,d],
    check the level by counting opening/closing brackets. 
    If not at least level four, look for the next pair.
    IF a level 5 pair is found

    Parameters
    ----------
    data : [type]
        [description]

    Returns
    -------
    [type]
        [description]
    """
    offset = 0
    for p in re.findall("\[\d+,\d+\]", data):
        # Gives a regex search object with span and start
        pair = re.search(re.escape(p), data[offset:])
        left_brackets = data[: pair.start() + offset].count("[")
        right_brackets = data[: pair.start() + offset].count("]")
        if left_brackets - right_brackets >= 4:
            x, y = pair.group()[1:-1].split(",")
            # split the string into two parts at the pair
            # flip left side around so we get the first num going backwards
            left = data[: pair.start() + offset][::-1]
            right = data[pair.end() + offset :]
            # look left
            search_left = re.search("\d+", left)
            if search_left:
                # need to find the rightmost match not the first
                amt = int(left[search_left.start() : search_left.end()][::-1]) + int(x)
                left = f"{left[:search_left.start()]}{str(amt)[::-1]}{left[search_left.end():]}"
            # look right
            search_right = re.search("\d+", right)
            if search_right:
                amt = int(right[search_right.start() : search_right.end()]) + int(y)
                right = (
                    f"{right[:search_right.start()]}{amt}{right[search_right.end():]}"
                )
            data = f"{left[::-1]}0{right}"
            break
        else:
            # offset = pair.end() + offset
            pass
    return data


"""
def explode(i, number, this_number):
    new_number = ""
    # Find left number
    for j, char in enumerate(number[i - 1 :: -1]):
        if j == 1 and char in [",", "]", "["]:
            new_number = number[: i - j - 1] + str(0)
        if char not in [",", "]", "["]:
            that_number = int(char)
            that_number = this_number + that_number
            new_number = number[: i - j - 1] + str(that_number) + number[i - j : i - 1]
            break

    # if no left number found copy whole string up to explode
    if char == "[":
        new_number = number[: i - 1]

    # get right number of pair
    off = 2
    if this_number > 9:
        off += 1
    if number[i + off + 1] in ["]", "[", ","]:
        right_pair_number = int(number[i + off])
    else:
        right_pair_number = int(number[i + off : i + off + 2])
        off += 1

    for j, char in enumerate(number[i + off + 1 :]):
        if char not in [",", "]", "["]:
            if number[i + off + j + 2] in [",", "]", "["]:
                right_number = int(char)
            else:
                right_number = int(number[i + off + j + 1 : i + off + j + 3])
            right_number += right_pair_number
            new_number += number[i + off : i + off + j + 1]
            new_number += str(right_number)
            new_number += number[i + off + j + 2 :]
            break

    if char == "]":
        new_number += number[i + off :]

    return new_number
"""

