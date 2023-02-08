# program to print all numbers in a range divisible bya given number

lower = int(input("Enter lower limit:"))
upper = int(input("Enter upper limit:"))
n = int(input("Enter the number to divide:"))
for i in range(lower, upper+1):
    if i % n == 0:
        print(i)
