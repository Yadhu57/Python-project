# 7. Right-Angled Pattern With Characters
n = int(input("Enter the number of rows"))
k = 1
for i in range(n):
    for j in range(i):
        print(chr(k + 64), end="")
        k += 1
    print()
