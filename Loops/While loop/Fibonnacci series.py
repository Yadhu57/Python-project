limit = int(input("Enter the limit "))
a = 0
b = 1
c = 0
while c <= limit:
    print(a, end=' ')
    sum = a + b
    a = b
    b = sum
    c += 1
