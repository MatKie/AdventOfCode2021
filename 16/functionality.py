import numpy as np


class Coder(object):
    def __init__(self, hexadec):
        """
        Coder doing these things:
            Decoding the hexcode to binary
            recursively search the binary for packages within
            calculating the hassum(?) of these packages acc. to packages
            acc. to rules given in question.

        Parameters
        ----------
        hexadec : str
            string in hexadecimal system
        """
        self.hexadec = hexadec
        self.bin = None
        self.versions, self.types, self.literals = [], [], []
        self.hex_to_bin = {
            "0": "0000",
            "1": "0001",
            "2": "0010",
            "3": "0011",
            "4": "0100",
            "5": "0101",
            "6": "0110",
            "7": "0111",
            "8": "1000",
            "9": "1001",
            "A": "1010",
            "B": "1011",
            "C": "1100",
            "D": "1101",
            "E": "1110",
            "F": "1111",
        }
        self.rules = {
            0: np.sum,
            1: np.prod,
            2: np.min,
            3: np.max,
            5: lambda x: 1 if x[0] > x[1] else 0,
            6: lambda x: 1 if x[0] < x[1] else 0,
            7: lambda x: 1 if x[0] == x[1] else 0,
        }

    def decode_hex(self):
        """
        Decode the hexcode
        """
        self.bin = self.hex_to_bin.get(self.hexadec[0])
        for char in self.hexadec[1:]:
            self.bin += self.hex_to_bin.get(char)

    def _process_binary(self, i, length, called=False):
        """
        Processing the binary of a package description recursively:
        Check version and type, if type isn't four check which kind 
        of package it is. 
        If it's a package with a specific length of subpackages, call
        this function with this specific length, if it's a package with 
        a specific number of subpackages (x), call this function x times
        with a lenght just enough to run the loop once.

        Whenever all values from the subpackages are retrieved, the 
        type specific operation is executed and the result appended 
        to the values (at this level of recursion) and given back 
        to the higher recursive level.

        Parameters
        ----------
        i : int
            current position in string
        length : int
            up until where to parse the string in this call.
            just long enough to start the while loop if called for a 
            distinct number of packages or the length specified by the
            subpackage.
        called : bool, optional
            boolean wheter or not this is the original call (maybe be unneccesary), 
            by default False

        Returns
        -------
        int, int-like
            returns position in the string and the values 
            (which might be a list or int)
        """
        values = []
        while i < length - 1:
            version = self.bin_to_dec(self.bin[i : i + 3])
            i += 3
            type = self.bin_to_dec(self.bin[i : i + 3])
            i += 3
            self.versions.append(version)
            self.types.append(type)
            # This is a bit heuristic but ensures that the while loop is
            # broken if we reached the last bit of the binary.
            if not called and length - i < 5:
                break
            if type == 4:
                this_binary = ""
                while self.bin[i] == "1":
                    this_binary += self.bin[i + 1 : i + 5]
                    i += 5
                this_binary += self.bin[i + 1 : i + 5]
                this_literal = self.bin_to_dec(this_binary)
                self.literals.append(this_literal)
                i += 5
                # If this is the outermost package
                # Go until string is divisible by four again..
                values.append(this_literal)
                if not called:
                    while (i + 1) % 4:
                        i += 1
            else:
                if self.bin[i] == "0":
                    # parse 15 bits that represent the total length in bits of the sub-packets
                    sub_package_length = self.bin_to_dec(self.bin[i + 1 : i + 16])
                    i += 16
                    these_values = []
                    i, these_values = self._process_binary(
                        i, i + sub_package_length, called=True
                    )
                    values.append(self.rules.get(type)(these_values))
                else:
                    # parse 11 bitst that represent the number of sub-packets immediately contained
                    sub_packages_number = self.bin_to_dec(self.bin[i + 1 : i + 12])
                    i += 12
                    these_values = []
                    for _ in range(sub_packages_number):
                        i, value = self._process_binary(i, i + 2, called=True)
                        these_values.append(value)
                    values.append(self.rules.get(type)(these_values))
        return i, values

    def process_binary(self):
        """
        Wrapper function for _process_binary: 
        Processing the binary of a package description recursively:
        Check version and type, if type isn't four check which kind 
        of package it is. 
        If it's a package with a specific length of subpackages, call
        this function with this specific length, if it's a package with 
        a specific number of subpackages (x), call this function x times
        with a lenght just enough to run the loop once.

        Whenever all values from the subpackages are retrieved, the 
        type specific operation is executed and the result appended 
        to the values (at this level of recursion) and given back 
        to the higher recursive level.
        """
        i = 0
        length = len(self.bin)
        i, values = self._process_binary(i, length)
        if isinstance(values, list):
            values = values[0]
        self.value = values

    @staticmethod
    def bin_to_dec(binary):
        """
        Simple binary to decimal converter

        Parameters
        ----------
        binary : string
            binary number

        Returns
        -------
        int
            decimal representation of binary
        """
        decimal = 0
        for i, bit in enumerate(reversed([int(char) for char in binary])):
            decimal += 2 ** i * bit

        return decimal
