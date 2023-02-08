# To update a tuple
# converting it to a mutable data type
tuple3 = (1, 2, 3, 4, "string", 1.5)
y = list(tuple3)  # converting to list
y[0] = "Changed"
print(y)
print(type(y))
tuple3 = tuple(y)  # converting back to tuple
print(tuple3)
print(type(tuple3))
