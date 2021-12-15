from functionality import Decoder, count_special_combinations, read_input


class TestReadInput:
    def test_input(self):
        input, output = read_input("exampleinput.txt")

        assert type(output) == list
        assert type(output[0]) == list
        assert len(output) == 10
        assert len(input[0]) == 10
        assert len(output[-1]) == 4

    def test_count_easy_number(self):
        input, output = read_input("exampleinput.txt")
        counter = count_special_combinations(output)
        assert counter == 26


class TestDecoder:
    def test_decode_codes(self):
        input, output = read_input("exampleinput.txt")
        results = [8394, 9781, 1197, 9361, 4873, 8418, 4548, 1625, 8717, 4315]
        for input_i, output_i, result in zip(input, output, results):
            ThisDecoder = Decoder(input_i, output_i)
            ThisDecoder.decode_easy_codes()
            ThisDecoder.decode_hard_codes()
            this_result = ThisDecoder.decode_output()
            assert this_result == result


TestDecoder().test_decode_codes()
