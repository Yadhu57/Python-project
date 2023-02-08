# 3.Write a Python function to calculate the factorial of a number (a non-negative integer).
# The function accepts the number as an argument.

def fact(f):
    i = 1
    sum = 1
    while i <= f:
        sum = sum * i
        i = i + 1
    return sum


print(fact(5))
