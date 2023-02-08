"""
1. write a program that takes one function that takes one argument that argument will be multiplied
 with a  unknown given number
"""
def myfnc(c):
    return lambda d: d * c


mydoubler = myfnc(2)
print(mydoubler(11))


