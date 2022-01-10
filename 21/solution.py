from functionality import deterministic_dice, DiracDice

score = deterministic_dice(8, 3)

print("***Part 1***")
print("Score: {:d}".format(int(score)))
Dice = DiracDice(8, 3)
universes = Dice.find_all_universes()
this_sum = sum(universes[0])
that_sum = sum(universes[1])

print("***Part 2***")
print("Winning Score: {:d}".format(int(max(this_sum, that_sum))))
print("Loosing Score: {:d}".format(int(min(this_sum, that_sum))))

