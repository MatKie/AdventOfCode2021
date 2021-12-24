from functionality import Coder

with open("input.txt", "r") as f:
    hex = f.readline().rstrip()


Decoder = Coder(hex)
Decoder.decode_hex()
Decoder.process_binary()

print("***Part 1***")
print("***Sum of version is: {:d}".format(int(sum(Decoder.versions))))

print(Decoder.versions, Decoder.types, Decoder.literals)
print(len(Decoder.versions), len(Decoder.types), len(Decoder.literals))

