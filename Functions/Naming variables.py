"""
Naming variables:
 If we operate with same variable name inside and outside the function, python will treat them as 2 separate variables,
 one available in the global scope and one available in the local scope
"""
# Eg:
x = 5


def fnc():
    x = 6
    print(x)


fnc()
print(x)
