from os import read
from functionality import (
    find_optimal_position_p2,
    read_input,
    find_optimal_position,
    find_cost,
    find_cost_p2,
)

input_vector = read_input("input.txt")

position = find_optimal_position(input_vector)
print(f"Optimal position is {position}.")

cost = find_cost(input_vector, position)
print(f"Optimal cost is {cost}.")

print("***Part 2***")

position = find_optimal_position_p2(input_vector)
print(f"Optimal position is {position}.")

cost = find_cost_p2(input_vector, position)
print(f"Optimal cost is {cost}.")

