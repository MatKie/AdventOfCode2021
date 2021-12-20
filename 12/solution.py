from os import read
from functionality import read_input, Graph

graph, _ = read_input("input.txt")

ThisGraph = Graph(graph)
paths = ThisGraph.find_all_paths_loop()

print("***Part 1 ***")
print("Number of paths is: {:d}".format(len(paths)))

print("***Part 2***")
paths = ThisGraph.find_part_2()
print("Number of paths is: {:d}".format(len(paths)))
