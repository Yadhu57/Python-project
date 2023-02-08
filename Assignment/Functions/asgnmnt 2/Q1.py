# 1.Write a Python program to access a function inside a function
def outer_fn(a, b):
    def inner_fn():
        c = a + b
        return c

    return inner_fn()


print(outer_fn(4, 5))
