def read_input(filename):
    """
    Read input and return character wise

    Parameters
    ----------
    filename : str
        filepath

    Returns
    -------
    list of list of characters
    """
    main_list = []
    with open(filename, "r") as f:
        for line in f:
            sub_list = [char for char in line.rstrip()]
            main_list.append(sub_list)

    return main_list


class LineParser(object):
    def __init__(self, line_list):
        """
        Analysese a single line for errors or incomplete input

        Parameters
        ----------
        line_list : a list of characters
        """
        self.line = line_list
        self.context_symbols = {"(": ")", "{": "}", "[": "]", "<": ">"}
        self.corrupted = False
        self.incomplete = False
        self.open_context = None
        self.closer = None
        self.error_char = None

    def check_line(self):
        """
        Make a list of context openers and if a closer is found check if it 
        closes the latest context; if not give an error. If there are
        open context at the end, mark as incomplete.

        Raises
        ------
        ValueError
            [description]
        """
        if not self.line[0] in self.context_symbols.keys():
            raise ValueError("First char not an opener!")
        else:
            act_opener = [self.line[0]]

        for char in self.line[1:]:
            if char in self.context_symbols.keys():
                act_opener.append(char)
            elif char == self.context_symbols.get(act_opener[-1]):
                act_opener = act_opener[:-1]
            else:
                self.corrupted = True
                self.error_char = char
                break

        if len(act_opener) > 0:
            self.open_context = act_opener
            self.incomplete = True

    def mend(self):
        closer = ""
        for opener in reversed(self.open_context):
            closer += self.context_symbols.get(opener)

        self.closer = closer


class TextFile(object):
    closer_dict = {")": 1, "]": 2, "}": 3, ">": 4}

    def __init__(self, lines_list):
        """
        Holds LineParser objects for all lines in the lines_list. 
        Holds aggregated data.

        Parameters
        ----------
        lines_list : list of list of chars
        """
        self.lines = [LineParser(line) for line in lines_list]
        self.n_corrupted = 0
        self.n_incomplete = 0
        self.error_value = 0
        self.error_dict = {")": 3, "]": 57, "}": 1197, ">": 25137}
        self.closer_scores = []

    def analyse_file(self):
        """
        Check each line and add up error value when encountered
        """
        for i, Line in reversed(list(enumerate(self.lines))):
            Line.check_line()
            if Line.corrupted:
                self.error_value += self.error_dict.get(Line.error_char, 0)
                self.n_corrupted += 1
                del self.lines[i]
            elif Line.incomplete:
                Line.mend()
                self.closer_scores.append(TextFile.rate_closer(Line.closer))

    @staticmethod
    def rate_closer(closer):
        """
        Closers are score as:
        score = 0
        for each char:
        multiply by 5
        add a certain value dep. on char


        Parameters
        ----------
        closer : str
            closing string

        Returns
        -------
        int
            closing value
        """
        score = 0
        for char in [char for char in closer]:
            score *= 5
            score += TextFile.closer_dict.get(char)

        return score

    def get_closing_score(self):
        """
        Sorts the list and picks the value in the middle (it's always
        a odd number list)

        Returns
        -------
        int
            median score
        """
        self.closer_scores = sorted(self.closer_scores)
        median_index = int(len(self.closer_scores) / 2)
        return self.closer_scores[median_index]
