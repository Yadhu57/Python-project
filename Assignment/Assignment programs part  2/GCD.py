from math import lcm

a = int(input("Enter first number"))
b = int(input("Enter second number"))                  # Formula = GCD (a,b) = [|a.b|]/[lcm(a,b)]
c = lcm(a, b)
prd = a * b
gcd = prd / c
print(" GCD of", a, ",", b, "=", gcd)
