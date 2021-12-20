from functionality import Folder


A = Folder("input.txt")
A.construct_matrix()
A.fold()
A.count_dots()

print("***part 1***")
# 364 is too low
print("***After one fold there are {:d} dots".format(A.dots))

print("***part 2***")
while A.folds != []:
    A.fold()
A.count_dots()
A.transform_matrix()
print("***After all folds there are {:d} dots".format(A.dots))
print("Final Matrix was translated and printed to output.txt!")
