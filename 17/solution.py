from functionality import find_max_solutions


print("***Part 1***")
with open("solution_part1.txt", "r") as f:
    for line in f:
        print(line)
        pass

print("***Part 2***")
xlim = (269, 292)
ylim = (-68, -44)
solution = (23, 67)
solutions = find_max_solutions(xlim, ylim, solution)
print("Number of possible solutions is {:d}".format(int(len(solutions))))
