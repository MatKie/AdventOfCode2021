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
        Polymerise by brute force.

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

    def polymerise_smarter(self, ThisSmartPolymer):
        """
        Calculate number of pairs in step n+1 by creating a new dict
        where each AB pair creates an AC and CB pair (if AB -> C).

        Parameters
        ----------
        ThisSmartPolymer : SmartPolymer object

        Returns
        -------
        SmartPolymer Object
            Object with updated pair_counts dictionary
        """
        temp_pair_count = {k: 0 for k, v in ThisSmartPolymer.pair_counts.items()}
        for pair, count in ThisSmartPolymer.pair_counts.items():
            char_1, char_2 = [char for char in pair]
            result = self.rules.get(pair)
            count = ThisSmartPolymer.pair_counts.get(pair)
            temp_pair_count[char_1 + result] += count
            temp_pair_count[result + char_2] += count
            ThisSmartPolymer.pair_counts[pair] = 0

        ThisSmartPolymer.pair_counts.update(temp_pair_count)
        return ThisSmartPolymer


class SmartPolymer(object):
    def __init__(self, start_polymer, rules):
        """
        SmartPolymer only keeping track of the number of pairs.

        Parameters
        ----------
        start_polymer : list
            starting polymer as a list of chars
        rules : dict
            dict of polymerisation rules, used to create pair dict.
        """
        self.pairs = [
            item_1 + item_2 for item_1, item_2 in zip(start_polymer, start_polymer[1:])
        ]
        self.pair_counts = {k: 0 for k, v in rules.items()}
        for pair in self.pairs:
            self.pair_counts[pair] += 1

    def count_items(self):
        """
        Count letters by adding the count of the first char of a pair to that
        letters count (each letter is in two pairs). 
        The very last char needs to be added manually.

        Returns
        -------
        int
            Final Score
        """
        letters = {
            letter: 0
            for letter in set(
                [char for pair in self.pair_counts.keys() for char in pair]
            )
        }
        for pair, count in self.pair_counts.items():
            char_1, _ = [char for char in pair]
            letters[char_1] += count

        _, last_char = [char for char in self.pairs[-1]]
        letters[last_char] += 1

        max_count = max(letters.values())
        min_count = min(letters.values())

        return max_count - min_count
