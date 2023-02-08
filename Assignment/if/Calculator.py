print("CALCULATOR")
print("Enter First Number")
x = int(input("x="))
print("Enter Second Number")
y = int(input("y="))
print("Choose which operation is to be performed")
print("a.Addition")
print("b.Subtraction")
print("c.Multiplication")
print("d.Division")
print("e.Modulus")
print("f.Comparison")
print("g.Assignment operation")
option = input("please enter your choice")
if option == "a":
    z = x + y
    print(z)
elif option == "b":
    z = x - y
    print(z)
elif option == "c":
    z = x * y
    print(z)
elif option == "d":
    z = x / y
    print(z)
elif option == "e":
    z = x % y
    print(z)
elif option == "f":
    if x == y:
        print("x=y")
    elif x < y:
        print("x<y")
    elif x > y:
        print("x>y")
    else:
        print("x!=y")
elif option == "g":
    x += y
    print("x+=y =", x)
    x -= y
    print("x-=y =", x)
    x **= y
    print("x**=y =", x)
    x //= y
    print("x//=y =", x)
    x %= y
    print("x%=y =", x)
else:
    print("please choose a valid option")
