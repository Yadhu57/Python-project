# 5.Finding the sum of even numbers using while loop
limit = int(input("enter the limit"))
i = 1
s = 0
while i <= limit:
    if i % 2 == 0:
        s = s + i
    i = i + 1
print("Sum of even numbers up to", limit, "=", s)
