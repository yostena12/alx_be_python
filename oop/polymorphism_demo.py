# polymorphism_demo.py

import math

# Base class
class Shape:
    def area(self):
        """Base method, should be overridden by subclasses"""
        raise NotImplementedError("Subclasses must override this method")


# Derived class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Override area to calculate rectangle area"""
        return self.length * self.width


# Derived class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Override area to calculate circle area"""
        return math.pi * (self.radius ** 2)
