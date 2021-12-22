from collections import Counter


def read_input(filename):
    """
    Read input. The rules and the starting string.

    Parameters
    ----------
    filename : str
        path to string

    Returns
    -------
    list of char and dictionary
        list of chars is the starting polymer and 
    """
    with open(filename, "r") as f:
        line = f.readline()
        start = [char for char in line.rstrip()]
        f.readline()

        rules = {}
        for line in f:
            line = line.rstrip()
            key, value = line.split(" -> ")
            rules.update({key: value})

        return start, rules


class Polymer(object):
    def __init__(self, start_polymer):
        """
        Polymer object holding a list and string representation of the 
        polymer as well as the monomer pairs.

        Parameters
        ----------
        start_polymer : [type]
            [description]
        """
        self.polymer = start_polymer
        self.pairs = [
            item_1 + item_2 for item_1, item_2 in zip(start_polymer, start_polymer[1:])
        ]
        self.count_monomers = None

    @property
    def string_representation(self):
        """
        Give back the polymer in string representation.

        Returns
        -------
        [type]
            [description]
        """
        string = self.polymer[0]
        for char in self.polymer[1:]:
            string += char
        return string

    def count_items(self):
        """
        Count the number of occurences of each monomer in the polymer. 
        Subtract the least abundant from the most abundant one. This
        is the final score.

        Returns
        -------
        int
            Final score.
        """
        self.count_monomers = Counter(self.polymer)
        max_count = max(self.count_monomers.values())
        min_count = min(self.count_monomers.values())

        return max_count - min_count


class Polymeriser(object):
    def __init__(self, rules):
        """
        Polymeriser applying the polymeriser rules to the Polymer

        Parameters
        ----------
        rules : dict
            which monomers combine to form a new polymer 
        """
        self.rules = rules

    def polymerise(self, ThisPolymer):
        """
        [summary]

        Parameters
        ----------
        ThisPolymer : Polymer object.
            Polymer object with the respective monomer pairs

        Returns
        -------
        Polymer object
            with the new polymer
        """
        new_polymer = []
        for item in ThisPolymer.pairs:
            item_1, item_2 = [char for char in item]
            new_polymer.extend([item_1, self.rules.get(item)])
        new_polymer.append(ThisPolymer.pairs[-1][-1])
        return Polymer(new_polymer)

