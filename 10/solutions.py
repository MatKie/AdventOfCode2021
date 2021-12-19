from os import read
from functionality import TextFile, read_input

text = read_input("input.txt")
TextObj = TextFile(text)

TextObj.analyse_file()

print("***Part 1***")
# 320253 too high
print("Error lines : {:d}".format(TextObj.n_corrupted))
print("Error value : {:d}".format(TextObj.error_value))

print("***Part 2***")
print("Autocorrect score : {:d}".format(TextObj.get_closing_score()))
