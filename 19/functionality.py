import numpy as np
from collections import Counter
from scipy.spatial.transform import Rotation


def read_input(filename):
    """
    Read the beacons of each sensor in a list of lists of tuples. 

    Parameters
    ----------
    filename : str
        path to input

    Returns
    -------
    list of list of tuples
        a list for each scanner
    """
    with open(filename, "r") as f:
        scanner_list = []
        this_scanner = []
        f.readline()
        for line in f:
            if line[:3] == "---":
                scanner_list.append(this_scanner)
                this_scanner = []
            elif line != "\n":
                line = line.rstrip()
                line = line.split(",")
                this_scanner.append(tuple(int(i) for i in line))
            else:
                pass
        scanner_list.append(this_scanner)

    return scanner_list


class Scanner(object):
    """
    Scanner object, holding the positions as an (N,3) array.

    Parameters
    ----------
    object : beacons
        list like 

    Methods:
    --------
    rotations: Generator going through the 24 possible rotations of the
    xyz coordinate system
    """

    def __init__(self, beacons):
        self.beacons = np.asarray(beacons, dtype=int)

    def rotations(self):
        """
        Generator function. Using scipy.spatial.transform.Rotation
        with the octahedral group (goes through all permutations of 
        cube rotations, right hand sided coordinate system.)

        Yields
        -------
        Yields a Scanner object with rotated coordinates 
        """
        Rotator = Rotation.create_group("O")
        for rotation in Rotator:
            rotated_coords = rotation.apply(self.beacons)
            yield Scanner(rotated_coords)


class Map(object):
    def __init__(self, scanner):
        """
        Map object, keeping track of all the beacons. 

        Parameters
        ----------
        scanner : One Scanner object which will be the (0,0,0) scanner. 
        """
        self.origin = scanner
        self.beacons = scanner.beacons
        self.beacon_set = set(tuple([round(ri) for ri in row]) for row in self.beacons)
        self.sensors = set((0, 0, 0))
        self.points = self.beacons.shape[0]
        self.min_overlap = 12

    def check_overlap(self, other):
        """
        Check if the 'other' scanner has overlap with the beacons in the map.

        Calc the distance of every point in the Map to all points in the 
        'other' scanners - check if there is one offset vector with 12 or
        more occurences; that is the offset of the 'other' scanner to the map.

        Parameters
        ----------
        other : Scanner
            Scanner not yet in the map

        Returns
        -------
        an offset if there is overlap and False if not
        """
        offsets = []
        for beacon_s in self.beacons:
            for beacon_o in other.beacons:
                # offsets.append(tuple(round(i) for i in np.subtract(beacon_s, beacon_o)))
                offsets.append(tuple(np.subtract(beacon_s, beacon_o)))

        occurences = Counter(offsets)
        for offset, occurence in occurences.items():
            if occurence >= self.min_overlap and offset != (0, 0, 0):
                return tuple(round(i) for i in offset)

        return False

    def __add__(self, other):
        return self.add(other)

    def __len__(self):
        return len(self.beacon_set)

    def add(self, other):
        """
        Add the scanner by checking if there is overlap between the Map
        and the Scanner in any rotation it can attain. 

        If there is, translate the points in the other scanner, 
        create a set of new points and add to the Map. Also add the 
        sensors by translating them.

        Parameters
        ----------
        other : [type]
            [description]

        Returns
        -------
        [type]
            [description]
        """
        for rotation in other.rotations():
            offset = self.check_overlap(rotation)
            if offset:
                translated_coordinates = rotation.beacons + np.ones_like(
                    rotation.beacons
                ) * np.asarray(offset)
                rotation_set = set(
                    tuple([round(ri) for ri in row]) for row in translated_coordinates
                )

                # Figure out new sets and nr of points
                add_points = rotation_set.difference(self.beacon_set)
                self.beacon_set = self.beacon_set.union(rotation_set)
                self.points = len(self.beacon_set)

                # Create new matrix with all unique points
                translated_coordinates = np.zeros((len(add_points), 3))
                for i, beacon in enumerate(add_points):
                    translated_coordinates[i, :] = np.asarray(beacon)
                self.beacons = np.concatenate((self.beacons, translated_coordinates))

                self.sensors.add(tuple(-i for i in offset))
                return True
        return False

    def max_sensor_distance(self):
        """
        Calc the manhatten distance for all sensors, get the laragest one.

        Returns
        -------
        float
            maximal manhatten distance between scanners.
        """
        # Double pass because set -- maybe more expensive to cast it to list.
        manhatten = []
        for sensor_i in self.sensors:
            for sensor_j in self.sensors:
                manhatten.append(np.sum(np.abs(np.subtract(sensor_i, sensor_j))))

        return int(max(manhatten))

