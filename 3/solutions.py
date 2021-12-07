import numpy as np
from classes_functions import BinaryArray, BinaryConverter, invert

# +
## Solution to task 1

with open('input.txt', 'r') as f:
    A = np.loadtxt(f, dtype=str)
    
# Create binary array and find dominant number
B = BinaryArray(A)
gamma_binary = B.dominant_binary

# Convert dominant binary number to decimal
gamma = BinaryConverter(gamma_binary).decimal

# Invert binary dominant number, and convert to decimal
epsilon_binary = invert(gamma_binary)
epsilon = BinaryConverter(epsilon_binary).decimal


print(f'The gamma rate is: {gamma}')
print(f'The epsilon rate is: {epsilon}')

print(f'The product is: {epsilon*gamma}')
# -


