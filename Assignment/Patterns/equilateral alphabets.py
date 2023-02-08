n = int(input("Enter the number of rows"))
for i in range(n):       # print spaces
    for j in range(n - i - 1):
        print(' ', end='')
    for k in range(2 * i + 1):       # print the 2n + 1 alphabets.
        print(chr(65 + k), end='')
    print()