from functionality import magnitude, process_number, add

snail_numbers = []
with open("input.txt", "r") as f:
    for line in f:
        snail_numbers.append(line.strip())

addition = add(snail_numbers[0], snail_numbers[1])
result = process_number(addition)


for snail_number in snail_numbers[2:]:
    addition = add(result, snail_number)
    result = process_number(addition)

print("***Part 1***")
print("Magnitude: {:d}".format(int(magnitude(result))))

largest_magnitude = 0
for i, first in enumerate(snail_numbers):
    for j, second in enumerate(snail_numbers):
        if i == j:
            continue
        addition = add(first, second)
        this_magnitude = magnitude(process_number(add(first, second)))

        if this_magnitude > largest_magnitude:
            largest_magnitude = this_magnitude

print("***Part 2***")
print("Largest Magnitude: {:d}".format(int(largest_magnitude)))
