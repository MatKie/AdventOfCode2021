import numpy as np


def read_input(filename):
    """
    Read input as seperate digits

    Parameters
    ----------
    filename : str
        path

    Returns
    -------
    np.ndarray
    """
    with open(filename, "r") as f:
        main_list = []
        for line in f:
            main_list.append([int(char) for char in line.rstrip()])

    return np.asarray(main_list)


class OctopusMap(object):
    def __init__(self, power_levels):
        """
        Holds the power levels of the octopuses and progresses them over time.

        Parameters
        ----------
        power_levels : np.ndarray
            Initial power levels
        """
        self.power_levels = power_levels
        self.n_step = 0
        self.n_flashes = 0
        self.synchronised = False  # if != False it holds n_step of first sync.
        self.size = power_levels.shape[0]

    def step_to_n(self, n):
        """
        Wrapper function to call self.step() to progress self.n_step to n
        """
        while self.n_step < n:
            self.step()

    def step(self):
        """
        Add one to all power levels then check if any octopus is ready to flash.
        Chose the first, flash it, and check again until there are no more
        flashable octopuses.
        """
        self.power_levels += np.ones_like(self.power_levels)

        flashes_left, flash_oct_x, flash_oct_y = self.next_flashing_position()

        while flashes_left:
            self.power_levels = self.flash(flash_oct_x, flash_oct_y)
            flashes_left, flash_oct_x, flash_oct_y = self.next_flashing_position()
            self.n_flashes += 1

        self.n_step += 1
        # Check if we are synchronised
        if np.sum(self.power_levels) == 0 and not self.synchronised:
            self.synchronised = self.n_step

    def next_flashing_position(self):
        """
        checks the array for power levels over 9 and gives first position
        where it's the case. Send abort signal if no more flashable octopuses.

        Returns
        -------
        bool, int, int
            boolean whether or not there are more flashes, int's are x, y
        """
        flashing_positions = np.where(self.power_levels > 9)
        if flashing_positions[0].shape[0] > 0:
            flash_oct_x, flash_oct_y = [item[0] for item in flashing_positions]
            flashes_left = True
            return flashes_left, flash_oct_x, flash_oct_y
        flashes_left = False
        return flashes_left, 0, 0

    def flash(self, flash_oct_x, flash_oct_y):
        """
        Flashes an octopus at position given by x and y. Checks if 
        adjacent position is in the array and not a zero (already flashed
        octopus in this step), then adds one to it.
        Finally assigns zero to the flashed octopus.

        Parameters
        ----------
        flash_oct_x : int
            x position of flashing octopus
        flash_oct_y : int
            y position of flashing octopus

        Returns
        -------
        np.ndarray
            Updated power_levels.
        """
        position = np.asarray((flash_oct_x, flash_oct_y))
        deviations = [
            np.asarray((-1, -1)),
            np.asarray((-1, 0)),
            np.asarray((-1, 1)),
            np.asarray((0, 1)),
            np.asarray((1, 1)),
            np.asarray((1, 0)),
            np.asarray((1, -1)),
            np.asarray((0, -1)),
        ]
        for deviation in deviations:
            this_position = position + deviation
            this_position = tuple(this_position)
            if -1 in this_position or self.size in this_position:
                continue
            elif self.power_levels[this_position] == 0:
                continue
            self.power_levels[this_position] += 1

        self.power_levels[tuple(position)] = 0

        return self.power_levels
