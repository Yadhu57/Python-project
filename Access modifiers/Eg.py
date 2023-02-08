# super class
class A:
    var1 = None  # public variable

    _var2 = None  # protected variable

    __var3 = None  # Private variable

    def _init_(self, var1, var2, var3):  # Constructor
        self.var1 = var1
        self._var2 = var2
        self.__var3 = var3

    def displayPublicMembers(self):  # public member function
        print("Public data member:", self.var1)  # Accessing public variable

    def _displayProtectedMembers(self):  # protected member function
        print("Protected Data Members:", self._var2)  # Accessing protected variable

    def __displayPrivateMembers(self):  # Private member function
        print("Private Data member:", self.__var3)  # Accessing private variable

    def accessPrivateMembers(self):  # public member function
        self.__displayPrivateMembers()


# Derived class
class B(A):

    def _init_(self, var1, var2, var3):  # Constructor
        A._init_(self, var1, var2, var3)

    def accessProtectedMembers(self):
        # Accessing protected member functions of super class
        self._displayProtectedMembers()


# creating objects of the derived class
obj = B("public_Red", "protected_White", "private_Green")

# calling public member functions of the class
obj.displayPublicMembers()
obj.accessProtectedMembers()
obj.accessPrivateMembers()


print("object is accessing public member:", obj.var1)   # Object can access public member
print("object is accessing protected member:", obj._var2) # Object can access Protected member
# Object can't access private member, so it will generate Attribute Error
# print(obj.__var3)
print(obj._A__var3) # Accessing Name Manngled variables
"""
Name Mangling

A process in which  any given identifier with one trailing underscore and two leading underscores is textually replaced 
with the  _ClassName__Identifier is known as Name Mangling.
"""
