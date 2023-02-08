def printme(*names):
    print("Type of passed arguments is", type(names))
    print("Printing the passed arguments...")
    for name in names:
        print(name)


printme("john", "david", "smith", "nick")
