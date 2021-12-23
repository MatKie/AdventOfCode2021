import numpy as np


def read_input(filename):
    """
    Read input and give back as numpy array.
    """
    with open(filename, "r") as f:
        main_list = []
        for line in f:
            main_list.append([int(char) for char in line.rstrip()])

    return np.asarray(main_list)


def transform_input(costs):
    """
    Transform input acc. to part 2 instructions, Essentially add copies
    onto a 5x5 grid, add 1 to array each time a move to left/down is made
    but if it's greater than 9, go back to start from 1

    Parameters
    ----------
    costs : np.ndarray
        old cost matrix

    Returns
    -------
    np.ndrarray
        new cost matrix.
    """
    n_rows, n_cols = costs.shape
    new_costs = np.zeros((5 * n_rows, 5 * n_cols))
    for row in range(5):
        for col in range(5):
            new_costs[
                row * n_rows : (row + 1) * n_rows, col * n_cols : (col + 1) * n_cols
            ] = costs + (np.ones_like(costs) * (row + col))

    new_costs = np.where(new_costs > 9, new_costs - 9, new_costs)
    return new_costs


class PathFinder(object):
    def __init__(self, costs):
        self.costs = costs
        self.n_rows, self.n_cols = costs.shape
        self.destination = (self.n_rows - 1, self.n_cols - 1)
        self.deviations = [
            np.asarray([0, -1]),
            np.asarray([-1, 0]),
            np.asarray([0, 1]),
            np.asarray([1, 0]),
        ]

    def dijkstra_algo(self, origin=(0, 0)):
        """
        Dijkstra algorithm:
        start out with a dictionary of unvisited nodes at infinite cost (except origin)
        start with origin as current node:
            -check all neighbours of current node: if not visited (init. state),
            and cost (value of cost matrix + cost of current node) is lower
            than cost the neighbours cost, overwrite neigbhours cost
            -mark current node as visited
            -check if current node was final node or all other unvisited
            nodes are at infinite cost (if so, break)
            -make the node which has lowest cost but is not yet visited the
            next current_node

        Parameters
        ----------
        origin : tuple, optional
            [description], by default (0, 0)

        Returns
        -------
        int
            cost of a path from origin to self.destination
        """
        # Assign a distance to all nodes equal to infinity except the origin equal to zero
        nodes = self.get_initial_nodes()
        nodes[origin] = [False, 0]
        # Initialise variables
        current_node = origin
        found_destination = False
        max_iter = max((self.n_rows, self.n_cols)) ** 2
        iteration = 0
        while not found_destination or iteration > max_iter + 1:
            iteration += 1
            if not iteration % 500:
                print("iteration {:d}...".format(iteration))
            neighbours = self.find_neighbours(current_node)
            current_cost = nodes[current_node][-1]
            for neighbour in neighbours:
                visited, distance = nodes.get(neighbour)
                if not visited:
                    this_distance = self.costs[neighbour] + current_cost
                    if distance > this_distance:
                        nodes[neighbour][1] = this_distance
            # mark as visited
            nodes[current_node][0] = True
            # find next node to visit (smallest distance, not visited)
            next_node = min(
                nodes, key=lambda key: np.inf if nodes[key][0] else nodes[key][1]
            )

            # Abort if we found destination or only inf is left (should not happen here)
            # If we don't break we start over with next node
            if current_node == self.destination:
                found_destination = True
            elif nodes[next_node][1] == np.inf:
                found_destination = True
            else:
                current_node = next_node

        return nodes[self.destination][-1]

    def get_initial_nodes(self):
        """
        Get initial node dictionary with all nodes unvisited and at
        infinite distance

        Returns
        -------
        dict
            See description
        """
        main_dict = {}
        for row in range(self.n_rows):
            for col in range(self.n_cols):
                # index: [visited?, distance]
                main_dict.update({(row, col): [False, np.infty]})
        return main_dict

    def find_neighbours(self, current_node):
        """
        Find all neighbours of current node 

        Parameters
        ----------
        current_node : tuple
            tuple of matrix indices

        Returns
        -------
        list of tuples
            all existing and accessible neigbhours. Some might be visited.
        """
        neighbours = []
        for deviation in self.deviations:
            deviation = np.asarray(current_node) + deviation
            if (
                -1 not in deviation
                and deviation[0] < self.n_rows
                and deviation[-1] < self.n_cols
            ):
                neighbours.append(tuple(deviation))

        return neighbours
