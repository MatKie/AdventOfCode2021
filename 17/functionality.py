import numpy as np


def find_max_solutions(xlim, ylim, best_solution):
    """
    Brute force your way through all possible solutions:
    Heuristics:
    y from best solution to solution immediately jumping towards 
    the most negative value.
    x from best solution (lowest value to reach xmin) to xmax (get to
    xmax in one shot).

    Parameters
    ----------
    xlim : tuple of int
        target area in x direction
    ylim : tuple of int
        target area in y direction
    best_solution : tuple of int
        Best solution from part 1

    Returns
    -------
    list of tuple
        all feasible solutions
    """
    solutions = []
    xmin, xmax = xlim
    ymin, ymax = ylim

    x_best, y_best = best_solution
    x_low = np.floor(-0.5 + np.sqrt(1 + 4 * xmin))

    for y in range(y_best, ymin - 1, -1):
        for x in range(x_best, xmax + 1):
            if Trajectory(x, y, xlim, ylim).hit:
                solutions.append((x, y))

    return solutions


class Trajectory(object):
    def __init__(self, x0, y0, xlim, ylim):
        """
        Trajectory calculator; checks if x0, y0 ends up in target area
        xlim, ylim

        Parameters
        ----------
        x0 : int
        y0 : int
        xlim : tuple of int
        ylim : tuple of int
        """
        self.x0 = x0
        self.y0 = y0
        self.xmin, self.xmax = xlim
        self.ymin, self.ymax = ylim
        self._t_solution = []
        self.tmax = 150
        self.hit = self.find_solution()

    @property
    def t_solution(self):
        if len(self._t_solution) == 1:
            return self._t_solution[0]
        else:
            return self._t_solution

    def find_solution(self):
        """
        Checks first if y will end up between min,max ylim and at 
        which time(s). Then checks if x is feasible at those times.

        Returns
        -------
        boolean
            whether or not it's a hit or not
        """
        y = 0
        t = 0
        y0 = self.y0
        yhit = False
        for t in range(self.tmax):
            y += y0
            y0 -= 1
            if y >= self.ymin and y <= self.ymax:
                self._t_solution.append(t + 1)
                yhit = True
            elif y < self.ymin:
                break

        if yhit:
            for t_solution in self._t_solution:
                if t_solution < self.x0:
                    c = -((self.x0 - t_solution) * (self.x0 - t_solution + 1.0)) / 2.0
                else:
                    c = 0

                x = (self.x0 * (self.x0 + 1.0)) / 2.0 + c
                if x >= self.xmin and x <= self.xmax:
                    return True
            return False
        return False

