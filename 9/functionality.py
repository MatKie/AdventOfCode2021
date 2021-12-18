import numpy as np


def read_input(filename):
    """
    Read input as an array of integers from 0-9

    Parameters
    ----------
    filename : str
        path to file

    Returns
    -------
    np.ndarray
        array with a 0-9 integer at every position acc. to input string
    """
    list_lines = []
    with open(filename, "r") as f:
        for line in f:
            list_lines.append([char for char in line.rstrip()])

    A = np.asarray(list_lines, dtype=int)
    return A


class AltMap(object):
    def __init__(self, array):
        self.org_map = array
        self.n_rows, self.n_cols = array.shape
        self.map = np.zeros((self.n_rows + 2, self.n_cols + 2))
        self.map[1:-1, 1:-1] = self.org_map
        self.low_index = None

    def derivatives(self):
        """
        Calculate the derivatives w.r.t. all four directions. The augmented
        array is used to calculate all derivatives with a matrix subtraction
        and subsequent cutting of the arrays.
        """
        # shape 6,12. First row is 0 - 1st and last row will be last_row - 0.
        self.down = self.map[:-1, :] - self.map[1:, :]
        # cut it to 5, 10 by eliminating first row as this one does not really
        # exist. Also the columns get cut.
        self.down = self.down[1:, 1:-1]
        # Set derivative of last row to a true like value
        self.down[-1, :] = -11

        # First row is 1st - 0 and last is 0 - last_row
        self.up = self.map[1:, :] - self.map[:-1, :]
        # cut it to 5, 10, by eliminating last row as this does not really exist
        self.up = self.up[:-1, 1:-1]
        # Set derivative of first row to a true like value
        self.up[0, :] = -11

        # shape 7, 11
        # first column is 1st - 0 and last is 0 - last_column
        self.left = self.map[:, 1:] - self.map[:, :-1]
        # Cut last column as this one doesn't really exist
        self.left = self.left[1:-1, :-1]
        # Set derivative of first column to a true like value
        self.left[:, 0] = -11
        # first column is 0 - first and last columns is last_colum - zero
        # eliminate first column as this one doesn't really exist
        self.right = self.map[:, :-1] - self.map[:, 1:]
        self.right = self.right[1:-1, 1:]
        # Set derivative of first column to a true like value
        self.right[:, -1] = -11

    def find_low_points(self):
        """
        Find the isolated low points and return the risk value of
        the map

        Returns
        -------
        float
            Risk value calculated from the low points acc. to question.
        """
        truth_array = np.where(
            self.up < 0,
            np.full_like(self.org_map, True, dtype=bool),
            np.full_like(self.org_map, False, dtype=bool),
        )
        for array in [self.down, self.left, self.right]:
            truth_array = np.where(
                np.logical_and(array < 0, truth_array == True),
                np.full_like(self.org_map, True, dtype=bool),
                np.full_like(self.org_map, False, dtype=bool),
            )

        self.low_index = np.where(truth_array == True)
        nr_risk_points = len(self.low_index[0])
        value_risk_points = np.sum(self.org_map[self.low_index])
        value_risk_points += nr_risk_points

        return value_risk_points

    def find_basin_value(self):
        """
        Find basin value by finding all unique clusters and then
        measuring their length. The product of the three largest ones
        is the final score.

        Returns
        -------
        float
            final score (basin value)
        """
        cluster_list = []
        for x, y in zip(*self.low_index):
            cluster = self._grow_cluster((x, y))
            cluster_list.append(cluster)

        cluster_list = self._merge_cluster(cluster_list)
        cluster_sizes = sorted([len(cluster) for cluster in cluster_list], reverse=True)

        basin_value = cluster_sizes[0] * cluster_sizes[1] * cluster_sizes[2]

        return basin_value

    def _merge_cluster(self, cluster_list):
        """
        Enumerate through reversed cluster list and delete item if it's found
        somewhere else in the list

        Parameters
        ----------
        cluster_list : list of sets
            a cluster for every low point we start with

        Returns
        -------
        list of sets
            all unique clusters
        """
        for i, cluster in reversed(list(enumerate(cluster_list))):
            if cluster in cluster_list[:i]:
                del cluster_list[i]

        return cluster_list

    def _grow_cluster(self, low_point):
        """
        Grow clusters by checking if a) the derivative is positive (defined
        as negative here) b) it's not on an edge and c) the value at
        the new position is not a 9.

        Parameters
        ----------
        low_point : tuple
            x,y coordinates of a low point foudn

        Returns
        -------
        cluster
            a set of tuples with positions.
        """
        cluster = set(((low_point, low_point)))
        new_points = [low_point]
        while new_points:
            dummy_new_points = []
            for new_point in new_points:
                x, y = new_point
                this_point = (x - 1, y)
                if self.up[new_point] < 0 and x > 0 and self.org_map[this_point] != 9:
                    dummy_new_points.append(this_point)
                this_point = (x + 1, y)
                if (
                    self.down[new_point] < 0
                    and x < self.n_rows - 1
                    and self.org_map[this_point] != 9
                ):
                    dummy_new_points.append(this_point)
                this_point = (x, y - 1)
                if self.left[new_point] < 0 and y > 0 and self.org_map[this_point] != 9:
                    dummy_new_points.append(this_point)
                this_point = (x, y + 1)
                if (
                    self.right[new_point] < 0
                    and y < self.n_cols - 1
                    and self.org_map[this_point] != 9
                ):
                    dummy_new_points.append((x, y + 1))
            new_points = dummy_new_points
            cluster = cluster.union(set(new_points))

        return cluster
