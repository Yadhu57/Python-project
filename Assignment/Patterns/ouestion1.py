rows = int(input("Enter number of rows: "))
for i in range(rows + 1):
    print(' ' * (rows - i) + '*  ' * (i + 1))
for i in reversed(range(rows)):
    print(' ' * (rows - i + 1) + '*  ' * (i + 1))

