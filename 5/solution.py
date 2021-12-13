from functionality import read_input, find_xy_max, Map

ventlines = read_input("input.txt")
x_max, y_max = find_xy_max(ventlines)

Map1 = Map(x_max, y_max)

for ventline in ventlines:
    Map1.mark_vent(ventline)

print(f"Crossing lines: {Map1.crossing_lines}")
