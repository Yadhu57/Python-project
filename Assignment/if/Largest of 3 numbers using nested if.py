a = int(input("Enter first number"))
b = int(input("Enter first number"))
c = int(input("Enter first number"))
if a > b:
    if a > c:
        print(" a is bigger")
elif b > a and b > c:
    print("b is bigger")
else:
    print("c is bigger")