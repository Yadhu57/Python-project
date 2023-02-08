# 1.Multiply all the numbers in a list using function
def mul(a):
    r = 1
    for i in a:
        r = r * i
        i += 1
    return r


print(mul(a=[1, 2, 3, 4, 5]))
