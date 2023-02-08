print("continue in while loop")
j = 1
while j <= 10:
    print(j)
    j = j + 1
    if j == 5:
        continue     # if condition is true else will also execute
else:
    print("Continued")