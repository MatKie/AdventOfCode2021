from functionality import AltMap, read_input

A = read_input("input.txt")
AMap = AltMap(A)
AMap.derivatives()

minimas = AMap.find_low_points()

# 346 is too low, 1565 is too high
print("***Part 1***")
print("Minimas: {:d}".format(minimas))

basin_value = AMap.find_basin_value()
print("***Part 2***")
print("Basin Value: {:d}".format(basin_value))

