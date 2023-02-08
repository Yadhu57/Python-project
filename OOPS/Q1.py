# find factorial of a number using class with function,arguments and return
class Fact:
    def factorial(self, n):
        f = 1
        for i in range(1, n+1):
            f = f*i
        return f
obj = Fact()
n = int(input("Enter a number"))
f = obj.factorial(n)
print('Factorial = ',f)