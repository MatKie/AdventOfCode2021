from functionality import read_input, Population

initial_population = read_input("input.txt")

FishPopulation = Population(initial_population)
FishPopulation.propagate_population(80)

print(f"The population has {FishPopulation.fish} fish after 80 days")

FishPopulation.propagate_population(256 - 80)

print(f"The population has {FishPopulation.fish} fish after 256 days")
