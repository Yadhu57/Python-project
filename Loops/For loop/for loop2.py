# pattern
row = int(input("enter the number of rows"))
for i in range(row+1):
    for j in range(i):
        print("*", end="")
    print()

# inverted pattern
rows = int(input("enter the number of rows"))
for i in range(rows+1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()