# 1.Half pyramid pattern with number
# rows = int(input("Enter number of rows: "))
rows = 5
for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print()
print("\n")

# 2. Reverse pattern from 10 to 1
# rows1 = 10
# for i in range(0, rows1 + 1):
#     for j in range(rows1 - i, 0, -1):
#         print(j, end=" ")
#     print()

# 3.full pyramid with star
# rows = int(input("Enter number of rows: "))
# for i in range(rows):
#     print(' '*(rows-i-1) + '*'*(2*i+1))
