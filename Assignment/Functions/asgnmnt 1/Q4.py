# 4. Write a Python function that takes a number as a parameter and check  the number is prime or not.
def prime(a):
    if a > 1:
        for i in range(2, a):
            if a % i == 0:
                print(a, "is not a prime number")
                break
        else:
            print(a, "is a prime number")
    else:
        print(a, "is not a prime number")


prime(9)
