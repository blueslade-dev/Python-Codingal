print("===== STAR PYRAMID PATTERN =====")

rows = int(input("Enter number of rows for star pattern: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("* ", end="")
    print()

print("\n===== FLOYD'S TRIANGLE =====")

rows = int(input("Enter number of rows for Floyd's Triangle: "))
number = 1

for i in range(1, rows + 1):
    for j in range(i):
        print(number, end=" ")
        number += 1
    print()

print("\n===== DIAMOND NUMBER PATTERN =====")

row_size = int(input("Enter number of rows for diamond pattern: "))

half_rows = (row_size + 1) // 2
space = half_rows - 1

for i in range(1, half_rows + 1):
    for j in range(space):
        print(" ", end="")

    space -= 1
    number = 1

    for j in range(2 * i - 1):
        print(number, end="")
        number += 1

    print()

space = 1

for i in range(1, half_rows):
    for j in range(space):
        print(" ", end="")

    space += 1
    number = 1

    for j in range(2 * (half_rows - i) - 1):
        print(number, end="")
        number += 1

    print()

print("\n===== LOOP ART DESIGN COMPLETE =====")
print("You created star, triangle, and diamond patterns using nested loops!")
