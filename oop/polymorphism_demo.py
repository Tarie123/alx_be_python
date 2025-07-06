# polymorphism_demo.py

import math

class Shape:
    def area(self):
        """Base method to compute area. Must be overridden."""
        raise NotImplementedError("Subclasses must implement this method.")

class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Compute area of rectangle."""
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Compute area of circle."""
        return math.pi * self.radius ** 2
