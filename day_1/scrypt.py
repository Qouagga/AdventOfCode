
import re

caloriesCarriedByEvles = []
caloriesCarriedByOneElf = []
ElfWithMostCalories = 0

with open('input.txt') as f:
    for line in f:
        if line != '\n':
            calories = re.match("(\d+)", line)
            caloriesCarriedByOneElf.append(int(calories.group(0)))
        else:
            caloriesCarriedByOneElf = sum(caloriesCarriedByOneElf)
            if ElfWithMostCalories < caloriesCarriedByOneElf:
                ElfWithMostCalories = caloriesCarriedByOneElf
            caloriesCarriedByEvles.append(caloriesCarriedByOneElf)
            caloriesCarriedByOneElf = []

    print("Puzzle n 1 :")
    print(ElfWithMostCalories)

    caloriesCarriedByEvles.sort(reverse=True)
    print("Puzzle n 2 :")
    print(sum(caloriesCarriedByEvles[0:3]))
