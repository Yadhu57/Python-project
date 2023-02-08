tuple4 = (1, 2, 3, 4, "string", 1.5)
y = list(tuple4)  # converting to list
y.append("Added")
print("list:", y)
tuple4 = tuple(y)
print("Tuple:", tuple4)

# Adding a tuple to another tuple
b = ("a", "b", "c")
tuple4 += b
print(tuple4)
