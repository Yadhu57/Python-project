# 4.Reversing a number using while loop in Python
n = int(input("Enter a number"))
r = 0
p = 1
s = 0
while n != 0:
    temp = n % 10
    r = r * 10 + temp
    p = p * temp
    s = s + temp
    n //= 10
print("Reverse = ", r)
print("Product od digits=", p)
print("Sum of digits = ", s)