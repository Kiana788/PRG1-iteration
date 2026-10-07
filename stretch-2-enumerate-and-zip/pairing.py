colours = ["red", "green", "blue"]
for index in range(len(colours)):
    print(f"{index}: {colours[index]}")

print("---")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age}")

print("---")

shortlist = ["Alice", "Bob"]

for name, age in zip(shortlist, ages):
    print(f"{name} is {age}")

from itertools import zip_longest

for name, age in zip_longest(shortlist, ages, fillvalue="(no name)"):
    print(f"{name} is {age}")
    
if len(shortlist) != len(ages):
    print("Warning: lists are different lengths")
