from functionality import read_input, OctopusMap

A = read_input("input.txt")
OctMap = OctopusMap(A)
OctMap.step_to_n(100)

print("***Part 1***")
print("We had {:d} flashes".format(OctMap.n_flashes))

while not OctMap.synchronised:
    OctMap.step()

print("***Part 2***")
print("At step {:d} all octopuses are synchronised".format(OctMap.synchronised))

