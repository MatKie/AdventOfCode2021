from functionality import read_input, Polymeriser, Polymer, SmartPolymer


start, rules = read_input("input.txt")
ThisPolymer = Polymer(start)

ThisPolymeriser = Polymeriser(rules)
for _ in range(10):
    ThisPolymer = ThisPolymeriser.polymerise(ThisPolymer)

print("***Part 1***")
print("The characteristic number is {:d}".format(ThisPolymer.count_items()))


start, rules = read_input("input.txt")
ThisPolymer = SmartPolymer(start, rules)

ThisPolymeriser = Polymeriser(rules)
for _ in range(40):
    ThisPolymer = ThisPolymeriser.polymerise_smarter(ThisPolymer)

print("***Part 2***")
print("The characteristic number is {:d}".format(ThisPolymer.count_items()))
