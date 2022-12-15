import bisect
from aoc_lib.aoc_read_input import read_input

data = read_input(2022, 1)
lines = [line for line in data.splitlines()]

calories = 0
list_of_calories = []
for line in lines:
    if line != "":
        value = int(line)
        calories += value
    else:
        bisect.insort(list_of_calories, calories)
        calories = 0
bisect.insort(list_of_calories, calories)


print(list_of_calories[-1])
print(sum(list_of_calories[-3:]))
