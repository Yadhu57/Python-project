def mul(l3):
    r = 1
    for i in l3:
        r = r * i
        i += i
    return r


print(mul(l3=[1, 2, 3, 4]))
