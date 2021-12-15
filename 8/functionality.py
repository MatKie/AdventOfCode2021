import numpy as np


def read_input(filename):
    """
    Parse input into two list of strings

    Parameters
    ----------
    filename : string
    
    Returns
    -------
    tuple of lists of list of strings
        innermost lists are:
        list of length 10 with first inputs, list of length 4 with
        second inputs.
    """
    input, output = [], []
    with open(filename, "r") as f:
        for line in f:
            line = line.split("|")
            this_input, this_output = [this_line.split() for this_line in line]
            input.append(this_input)
            output.append(this_output)

    return input, output


def count_special_combinations(array):
    """
    Count the number of occurrences of 'easy' values with unique 
    number of lit segments (1 has 2 segments, 7 has 3, 4 has four, 8 has 7)

    Parameters
    ----------
    array : list of list of strings

    Returns
    -------
    int
    """
    counter = 0
    for output in array:
        for word in output:
            if len(word) in [2, 3, 4, 7]:
                counter += 1

    return counter


class Decoder(object):
    def __init__(self, input, output):
        self.input_encoded = input
        self.output_encoded = output
        self.codes = {}
        self.easy_codes = {2: 1, 3: 7, 4: 4, 7: 8}
        self.inv_codes = None

    def decode_easy_codes(self):
        for item in self.input_encoded + self.output_encoded:
            coded_length = len(item)
            if coded_length in self.codes.keys():
                continue
            elif coded_length in self.easy_codes.keys():
                self._update_dict(item, self.easy_codes.get(coded_length))
            # Create inversely mapped codes
            self.inv_codes = {v: k for k, v in self.codes.items()}

    def _update_dict(self, item, number):
        update_dict = {frozenset(item): number}
        self.codes.update(update_dict)

    def decode_hard_codes(self):
        for item in self.input_encoded + self.output_encoded:
            coded_length = len(item)
            if coded_length in self.codes.keys():
                continue
            this_number = frozenset(item)
            if coded_length == 6:
                if self.inv_codes.get(4) - this_number == set():
                    self._update_dict(item, 9)
                elif self.inv_codes.get(1) - this_number != set():
                    self._update_dict(item, 6)
                else:
                    self._update_dict(item, 0)
            elif coded_length == 5:
                if self.inv_codes.get(7) - this_number == set():
                    self._update_dict(item, 3)
                elif len(self.inv_codes.get(4) - this_number) == 1:
                    self._update_dict(item, 5)
                elif len(self.inv_codes.get(4) - this_number) == 2:
                    self._update_dict(item, 2)
            # Update inversely mapped codes
            self.inv_codes = {v: k for k, v in self.codes.items()}

    def decode_output(self):
        decoded = ""
        for item in self.output_encoded:
            decoded += str(self.codes.get(frozenset(item)))
        decoded = int(decoded)
        return decoded

