# prime = [x for x in range(2, 21) if all(x % y != 0 for y in range(2, x))]
# print(prime)
#
# even = [i for i in range(101) if i % 2 == 0]
# print(even)
#
# odd = [j for j in range(101) if j % 2 != 0]
# print(odd)
#
# letters = [letter for letter in 'orange']
# print(letters)

"""
list comprehension provides an easy way to         it creates a new list  in which each element is the result of 
"""
n = int(input("Enter the limit"))
lst1 = [i for i in range(1, n) if i % 2 == 0]
print(lst1)