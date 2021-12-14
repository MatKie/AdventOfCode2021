import numpy as np


def read_input(filename):
    """
    Read input into np.ndarray (vector)

    Parameters
    ----------
    filename : string
        path to file

    Returns
    -------
    np.ndarray
        vector shape
    """
    with open(filename, "r") as f:
        vector = np.loadtxt(f, delimiter=",")

    return vector


def find_cost(array, position):
    """
    Calcultes the cost to move all crab submaries to a position

    Parameters
    ----------
    array : np.ndarray
        position of crab submarines
    position : int
        position to move to

    Returns
    -------
    int
        fuel cost
    """
    return np.sum(np.abs(array - position))


def find_optimal_position(array):
    """
    Finds optimal position to move to, needing the lowest amount of fuel.
    This position is the median. Going one to the left or right
    of the median changes value by +- 1 for all items -- except the middle 
    one which has to do plus 1. 

    Found by trying/intuition, checked with the internet.

    Parameters
    ----------
    array : np.ndarray
        position of crab submaries

    Returns
    -------
    int
        optimal position to move to
    """
    position = np.median(array)
    if find_cost(array, np.floor(position)) < find_cost(array, np.ceil(position)):
        opt_position = np.floor(position)
    else:
        opt_position = np.ceil(position)
    return opt_position


def find_cost_p2(array, position):
    """
    Calcultes the cost to move all crab submaries to a position if 
    each additional move costs one additional fuel.

    tot fuel    1 3   6 15  21 28
    position    1 2   3 4   5  6
    multiplier  1 1.5 2 2.5 3  3.5

    --> tot fuel = position * (position/2 + 0.5)

    Parameters
    ----------
    array : np.ndarray
        position of crab submarines
    position : int
        position to move to

    Returns
    -------
    int
        fuel cost
    """
    distances = np.abs(array - position)
    distances_over_2 = distances / 2 + 0.5
    return np.sum(distances * distances_over_2)


def find_optimal_position_p2(array):
    """
    Finds optimal position to move to, needing the lowest amount of fuel.
    This position is the average (ceil or floor of it). Found by intuition.
    Proof:
    https://www.reddit.com/r/adventofcode/comments/rawxad/2021_day_7_part_2_i_wrote_a_paper_on_todays/

    Parameters
    ----------
    array : np.ndarray
        position of crab submaries

    Returns
    -------
    int
        optimal position to move to
    """
    position = np.mean(array)
    if find_cost_p2(array, np.floor(position)) < find_cost_p2(array, np.ceil(position)):
        opt_position = np.floor(position)
    else:
        opt_position = np.ceil(position)
    return opt_position
