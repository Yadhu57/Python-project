print("break in while loop")
m = 1
while m <= 10:
    print(m)
    m = m + 1
    if m == 5:
        break
else:                 # else will not execute if break condition is true
    print("breaked")