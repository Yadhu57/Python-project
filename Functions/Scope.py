"""
Local scope:
 A variable created inside a function belongs to the local scope of that function,and can only be used inside
 that function
"""


# Eg:
def fnc():
    x = 5  # Local variable
    print(x)


fnc()
# print(x)    # can't be used outside the function

"""
Global scope:
 A variable created in the main body of the code is a global variable and belongs to the global scope
"""
# Eg:
y = 6   # Global variable


def fn2():
    print(y)


fn2()
print(y)
