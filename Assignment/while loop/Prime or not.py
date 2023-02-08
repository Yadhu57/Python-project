# 6.check whether a number is prime or not using while loop
n = int(input("Enter a number"))
p = 0
i = 2
while i < n:
    if n % i == 0:
        p = 1
        break
    i = i+1
if p == 0:
    print("\n",  n, " is a Prime Number")
else:
    print("\n", n, " is not a Prime Number")

