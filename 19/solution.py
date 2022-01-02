from functionality import read_input, Scanner, Map

scanner_list = read_input("input.txt")
Scanners = [Scanner(this_scanner) for this_scanner in scanner_list]

ThisMap = Map(Scanners[0])

not_added = [i for i in range(1, len(Scanners))]
j = 0
while len(not_added) > 0 and j < 100:
    while_added = []
    for i, ThatScanner in enumerate(Scanners):
        if i in not_added:
            success = ThisMap.add(ThatScanner)
        else:
            success = True
        if not success:
            while_added.append(i)
    not_added = while_added
    j += 1

print("***Part 1***")
# 832 is too high
print("Nr of beacons: {:d}".format(len(ThisMap)))
print("***Part 2***")
print("Max Distance between sensors: {:d}".format(ThisMap.max_sensor_distance()))
