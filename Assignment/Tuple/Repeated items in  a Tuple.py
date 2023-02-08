# 3.Write a python program to find repeated items from a tuple
tuple1 = ('a', 'b', 'c',  'd', 'e', 'b', 'a', 'd', 'c', 'f', 1, 1, 2, 3, 4, 4, 5)
a = []
for i in tuple1:
    if tuple1.count(i) > 1:
        a.append(i)
print("Repeated items in the tuple:", a)

