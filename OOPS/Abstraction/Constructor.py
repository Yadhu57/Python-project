"""
                                         Constructor
constructors are member functions of a class which will automatically executed when an object of a class is created
constructors don't have return value

we can define constructor as
def __init__(self)

mainly 2 types of constructors
1. non parameterised constructor/default constructor
2. parameterised constructor
"""


# 1.Non parameterised constructor
class A:
    def __init__(self):
        print('Non parameterised constructor')


ob = A()
print("\n")


# 2.parameterised constructor
class B:
    def __init__(self, name):
        print("parameterised constructor")
        self.na = name

    def display(self):
        print('Name is:', self.na)


obj = B('Arun')
obj.display()
