# 2. write a program to filter a list of intigers using lambda
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = list(filter(lambda a: a % 2 == 0, lst))
print(even)
odd = list(filter(lambda a: a % 2 != 0,lst))
print(odd)

#-----------------------------------------------------

maxi = lambda x, y: x if (x > y) else y
print(maxi(5, 8))
