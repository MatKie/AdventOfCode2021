from functionality import read_input, count_special_combinations, Decoder

print("*** Part 1***")
input, output = read_input("input.txt")
counter = count_special_combinations(output)

print(f"Number of special occurrences is {counter}")

print("*** Part 2***")
input, output = read_input("input.txt")
sum = 0
for input_i, output_i in zip(input, output):
    ThisDecoder = Decoder(input_i, output_i)
    ThisDecoder.decode_easy_codes()
    ThisDecoder.decode_hard_codes()
    this_result = ThisDecoder.decode_output()
    sum += this_result

print(f"The sum of all encoded number is {sum}")

