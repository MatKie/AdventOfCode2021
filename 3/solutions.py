import numpy as np
from classes_functions import BinaryArray, BinaryConverter, invert
from classes_functions import find_scrubber_number
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
# +

oxygen_rating_binary = find_scrubber_number(B)
oxygen_rating = BinaryConverter(oxygen_rating_binary).decimal

B_invert = BinaryArray(A, do_invert=True)

co2_rating_binary = find_scrubber_number(B_invert)
co2_rating = BinaryConverter(co2_rating_binary).decimal

print(f'The oxygen rating is: {oxygen_rating}')
print(f'The co2 scrubber rate is: {co2_rating}')
print(f'Life support rating (product) is: {oxygen_rating*co2_rating}') 
