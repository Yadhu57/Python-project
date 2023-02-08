def add():
    print(a + b)


def sub():
    print(a - b)


def mul():
    print(a * b)


def div():
    print(a / b)


a = int(input("enter first number"))
b = int(input("Enter second Number"))
c = input("Which Operation is to be performed (+, -, /, *)")
if c == "+":
    add()
elif c == "-":
    sub()
elif c == "*":
    mul()
elif c == "/":
    div()
else:
    print("Enter valid operation")