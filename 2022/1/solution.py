import bisect
import aocd

data = aocd.get_data(day=1, year=2022)
lines = [line for line in aocd.get_data(day=1, year=2022).splitlines()]

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