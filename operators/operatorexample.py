# Arithmetic operators: + -  % * /
from typing import List

print("Arithmetic operators")
a = 6
b = 5
print("addition:", a + b)
print("subtraction:", a - b)
print("multiplication:", a * b)
print("division:", a / b)
print("modulus:", a % b)

# Assignment operators: =  +=  -+  *=  **=  /=  %= //=
print("Assignment operators")
x = 3
r = 3
x += r
print(x)
x -= 4
print(x)
x //= 1
print(x)
x %= 4
print(x)
x **= 3
print(x)

# comparison operators: == != <= >= > <
print("comparison operators")
y = 5
s = 5
print(y == s)
print(y != s)
print(y >= s)
print(y <= s)
print(y > s)
print(y < s)

# Logical operators: and or not
print("Logical operators")
d = 5
print(4 < d and d < 7)
print(6 > d or d < 10)
print(not (3 < d and d < 10))
# Bitwise operators
# Identity operators: is, is not
print("Identity operators")
h = ['orange', 'banana']
j = ['mango', 'apple']
l = 5
n = 5
k = h is not j
m = l is n
print(k)
print(m)
print(type(h))
# Membership operator:in,not in
print(" Membership operator")
u = ['mango', 'apple']
print('mango' in u)
print('orange' not in u)

#assignment -make a calculator