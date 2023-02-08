# 5. Create an inner function to calculate the addition in the following way
# •	Create an outer function that will accept two parameters, a and b
# •	Create an inner function inside an outer function that will calculate the addition of a and b
# •	At last, an outer function will add 5 into addition and return it

def outer_function(a, b):
    def inner_function():
        c = a + b
        return c
    return inner_function() + 5


print(outer_function(5, 6))
