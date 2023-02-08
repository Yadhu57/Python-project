# 7.Print even and odd numbers between 1 to the entered number
limit = int(input("Enter the limit"))
odd = []
even = []
i = 1
while i <= limit:
    if i % 2 == 0:
        odd.append(i)
    else:
        even.append(i)
    i = i + 1
print("Odd numbers =", odd)
print("Even numbers =", even)
