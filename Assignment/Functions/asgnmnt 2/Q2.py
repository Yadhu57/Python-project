# 2.Write a Python function to create and print a list where the values are square of numbers
# between 1 and 30 (both included).
def squares():
    l1 = []
    for i in range(1, 31):
        l1.append(i ** 2)
    return l1


print(squares())
