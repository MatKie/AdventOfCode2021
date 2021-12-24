from functionality import Coder

with open("input.txt", "r") as f:
    hex = f.readline().rstrip()


Decoder = Coder(hex)
Decoder.decode_hex()
Decoder.process_binary()

print("***Part 1***")
print("Sum of version is: {:d}".format(int(sum(Decoder.versions))))


print("***Part 2***")
print("Final value is: {:d}".format(int(Decoder.value)))

