from functionality import read_input, find_xy_max, Map

ventlines = read_input("input.txt")
x_max, y_max = find_xy_max(ventlines)

Map1 = Map(x_max, y_max)

for ventline in ventlines:
    Map1.mark_vent(ventline, diagonals=False)

print(f"Crossing lines: {Map1.crossing_lines}")

Map2 = Map(x_max, y_max)
for ventline in ventlines:
    Map2.mark_vent(ventline, diagonals=True)

print(f"Crossing lines: {Map2.crossing_lines}")
