def getsum(num):
    if num == 1:
        return 1
    print(num)
    print(getsum(num - 1))
    return num + getsum(num - 1)
num = 10
