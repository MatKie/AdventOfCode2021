from functionality import PathFinder, read_input, transform_input


A = read_input("input.txt")
ThisPath = PathFinder(A)

total_cost = ThisPath.dijkstra_algo()
# total_cost = 769

print("***Part 1***")
print("Total Cost: {:d}".format(total_cost))

A = read_input("input.txt")
A = transform_input(A)
ThisPath = PathFinder(A)

total_cost = ThisPath.dijkstra_algo()

print("***Part 1***")
print(total_cost)
print("Total Cost: {:f}".format(total_cost))
# 2963
