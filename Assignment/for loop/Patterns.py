# 4. inverted full pyramid with star
size = 7
m = (2 * size) - 2
for i in range(size, 0, -1):
    for j in range(0, m):
        print(end=" ")
    # decrementing m after each loop
    m = m + 1
    for j in range(0, i - 1):
        print("* ", end=' ')
    print(" ")

# 5.Half pyramid pattern with number
rows = int(input("Enter the number of rows"))
for i in range(rows):
    for j in range(i + 1):
        print(j+1, end=" ")
    print()
print("\n")

# 2. Reverse pattern from 10 to 1
print("Reverse pattern from 10 to 1")
print("\n")
rows1 = 10
for i in range(0, rows1 + 1):
    for j in range(rows1 - i, 0, -1):
        print(j, end=" ")
    print()