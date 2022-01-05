from os import read
import numpy as np
from functionality import read_input, PictureEnhancer

code, picture = read_input("input.txt")
PE = PictureEnhancer(code)
for i in range(2):
    print(i)
    picture = PE.enhance_picture(picture, i)

print("***Part 1***")
# 5573
print("There are {:d} light pixel in the picture").format(int(np.sum(picture)))

for i in range(2, 50):
    print(i)
    picture = PE.enhance_picture(picture, i)

print("***Part 2***")
# 20097
print("There are {:d} light pixel in the picture").format(int(np.sum(picture)))
