for row in range(1, 4):
    for column in range(1, 4):
        print(f"{row} x {column} = {row * column}")
    print()


total_printed = 0
for row in range(1, 5):
    for column in range(1, 3):
        total_printed = total_printed + 1
print(total_printed)

for row in range(1, 4):
    if row % 2 == 0:
        for column in range(1, 4):
            print(f"{row} x {column} = {row * column}")
        print()
