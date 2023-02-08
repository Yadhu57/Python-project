# Eg1:
x = lambda a, b: a + b
print(x(5, 6))

#_____________________________________________________________\

# Eg2:
def myfnc(c):
    return lambda d: d * c


mydoubler = myfnc(2)
print(mydoubler(11))
