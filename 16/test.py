import pytest
from functionality import Coder


class TestDecoder:
    def test_hexcodes_decoding(self):
        hex = "D2FE28"
        Decoder = Coder(hex)
        Decoder.decode_hex()

        assert Decoder.bin == "110100101111111000101000"

        hex2 = "EE00D40C823060"
        Decoder = Coder(hex2)
        Decoder.decode_hex()

        assert Decoder.bin == "11101110000000001101010000001100100000100011000001100000"

    def test_to_binary(self):
        assert Coder.bin_to_dec("0001") == 1
        assert Coder.bin_to_dec("00011") == 3
        assert Coder.bin_to_dec("01010") == 10

    def test_process_type_four(self):
        hex = "D2FE28"
        Decoder = Coder(hex)
        Decoder.decode_hex()

        Decoder.process_binary()

        print(Decoder.versions, Decoder.types, Decoder.literals)

        assert Decoder.versions[0] == 6
        assert Decoder.types[0] == 4
        assert Decoder.literals[0] == 2021

    def test_process_subpackage_length(self):
        hex = "38006F45291200"
        Decoder = Coder(hex)
        Decoder.decode_hex()

        Decoder.process_binary()

        print(Decoder.versions, Decoder.types, Decoder.literals)

        assert Decoder.literals == [10, 20]

    def test_process_subpackage_number(self):
        hex = "EE00D40C823060"
        Decoder = Coder(hex)
        Decoder.decode_hex()

        Decoder.process_binary()

        print(Decoder.versions, Decoder.types, Decoder.literals)

        assert Decoder.literals == [1, 2, 3]

    def test_combination_1(self):
        hex = "8A004A801A8002F478"
        Decoder = Coder(hex)
        Decoder.decode_hex()
        Decoder.process_binary()
        assert sum(Decoder.versions) == 16

    def test_combination_2(self):
        hex = "620080001611562C8802118E34"
        Decoder = Coder(hex)
        Decoder.decode_hex()
        Decoder.process_binary()
        assert sum(Decoder.versions) == 12

    def test_combination_3(self):
        hex = "C0015000016115A2E0802F182340"
        Decoder = Coder(hex)
        Decoder.decode_hex()
        Decoder.process_binary()
        assert sum(Decoder.versions) == 23

    def test_combination_4(self):
        hex = "A0016C880162017C3686B18A3D4780"
        Decoder = Coder(hex)
        Decoder.decode_hex()
        Decoder.process_binary()
        assert sum(Decoder.versions) == 31


class TestPart2(object):
    def test_combination_1(self):
        hex = "C200B40A82"
        Decoder = Coder(hex)
        Decoder.decode_hex()
        Decoder.process_binary()
        assert Decoder.value == 3

    def test_combination_2(self):
        hex = "04005AC33890"
        Decoder = Coder(hex)
        Decoder.decode_hex()
        Decoder.process_binary()
        assert Decoder.value == 54

    def test_combination_3(self):
        hex = "880086C3E88112"
        Decoder = Coder(hex)
        Decoder.decode_hex()
        Decoder.process_binary()
        assert Decoder.value == 7

    def test_combination_4(self):
        hex = "CE00C43D881120"
        Decoder = Coder(hex)
        Decoder.decode_hex()
        Decoder.process_binary()
        assert Decoder.value == 9

    def test_combination_5(self):
        hex = "D8005AC2A8F0"
        Decoder = Coder(hex)
        Decoder.decode_hex()
        Decoder.process_binary()
        assert Decoder.value == 15

    def test_combination_6(self):
        hex = "F600BC2D8F"
        Decoder = Coder(hex)
        Decoder.decode_hex()
        Decoder.process_binary()
        assert Decoder.value == 15

    def test_combination_7(self):
        hex = "9C005AC2F8F0"
        Decoder = Coder(hex)
        Decoder.decode_hex()
        Decoder.process_binary()
        assert Decoder.value == 15

    def test_combination_8(self):
        hex = "9C0141080250320F1802104A08"
        Decoder = Coder(hex)
        Decoder.decode_hex()
        Decoder.process_binary()
        assert Decoder.value == 1


TestPart2().test_combination_8()
