# 1.Define a function that accepts a number and returns whether the number is even or odd.
def odd_even(a):
    if a % 2 == 0:
        print("Even")
    else:
        print("Odd")


a = int(input("Enter a number"))
odd_even(a)
