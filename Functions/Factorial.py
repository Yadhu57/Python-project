# write a program to find factorial of a number using function with return type a nd function parameter

def fact(n):
    i = 1
    sum = 1
    while i <= n:
        sum = sum * i
        i = i + 1
    return sum


print(fact(n=int(input("Enter a number"))))

