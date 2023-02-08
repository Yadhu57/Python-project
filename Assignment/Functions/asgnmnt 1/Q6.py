"""
6. Generate a Python list of all the even numbers between 4 to 30
Expected o/p:
[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
 Hint:
•	Use the built-in function range() to generate the sequence of numbers between the given start number to the
    stop number with a step = 2 to get even numbers.
•	pass range() function to a list constructor to create a list
"""


def even():
    l1 = []
    for i in range(4, 30):
        if i % 2 == 0:
            l1.append(i)

    return l1


print(even())
