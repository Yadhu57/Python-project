"""
 abstraction is to represent.....

* main advantage is data hiding
* Python provides abc(Abstract base classes)module to use abstraction
* The ABC works by decorating methods of the base class as abstract
"""
from abc import ABC, abstractmethod


# Abstract class

class polygon(ABC):
    @abstractmethod
    def sides(self):
        pass

    def display(self):
        print("non abstract method")


class Triangle(polygon):
    def sides(self):
        print("Triangle has 3 sides")


t = Triangle()
t.sides()
t.display()
