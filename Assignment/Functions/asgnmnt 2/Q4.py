# 4.Generate a Python list of all the even numbers between 4 and 30
def even():
    l1 = []
    for i in range(4, 30):
        if i % 2 == 0:
            l1.append(i)

    return l1


print(even())
