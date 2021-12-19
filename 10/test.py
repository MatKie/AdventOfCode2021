from os import read
from typing import Text
import pytest
from functionality import LineParser, TextFile, read_input


class TestInput:
    def test_read_input(self):
        main_list = read_input("exampleinput.txt")
        print(main_list)

        assert main_list[2][3] == "("
        assert main_list[2][4] == "<"


class TestLineParser:
    def test_line_parser(self):
        line = ["(", "[", "]", ")", "<", ">", "{", "(", "[", "}", ")"]
        Line = LineParser(line)
        Line.check_line()

        assert Line.corrupted == True
        assert Line.error_char == "}"

    def test_line_parser2(self):
        line = [
            "[",
            "<",
            "(",
            "<",
            "(",
            "<",
            "(",
            "<",
            "{",
            "}",
            ")",
            ")",
            ">",
            "<",
            "(",
            "[",
            "]",
            "(",
            "[",
            "]",
            "(",
            ")",
        ]
        Line = LineParser(line)
        Line.check_line()

        assert Line.corrupted == True
        assert Line.error_char == ")"

    def test_line_parser_incomplete(self):
        line = ["(", "[", "]", "<", ">", "{", "(", "[", "]", ")", "<"]
        Line = LineParser(line)
        Line.check_line()

        assert Line.corrupted == False
        assert Line.incomplete == True

    def test_line_parser_detail(self):
        text = read_input("exampleinput.txt")

        for i, error in zip([2, 4, 5, 7, 8], ["}", ")", "]", ")", ">"]):
            Line = LineParser(text[i])
            Line.check_line()

            assert Line.corrupted == True
            assert Line.error_char == error


class TestTextFile:
    def test_error_score(self):
        main_list = read_input("exampleinput.txt")
        ThisText = TextFile(main_list)
        ThisText.analyse_file()

        assert ThisText.error_value == 26397

    def test_rate_closer(self):
        closer = "}}]])})]"
        closing_score = TextFile.rate_closer(closer)

        assert closing_score == 288957

    def test_closing_char(self):
        text = read_input("exampleinput.txt")

        for i, error in zip(
            [0, 1, 3, 6, 9], ["}}]])})]", ")}>]})", "}}>}>))))", "]]}}]}]}>", "])}>"]
        ):
            Line = LineParser(text[i])
            Line.check_line()
            Line.mend()
            print(Line.closer)
            assert Line.incomplete == True
            assert Line.closer == error

    def test_closing_score(self):
        text = read_input("exampleinput.txt")

        AllText = TextFile(text)
        AllText.analyse_file()

        print(AllText.get_closing_score())
        print(AllText.closer_scores)
        assert AllText.get_closing_score() == 288957

