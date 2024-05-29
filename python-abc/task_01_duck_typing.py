#!/usr/bin/python3
from abc import ABC, abstractmethod
import math

# Define the abstract base class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# Define the Circle class
class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

# Define the Rectangle class
class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Define the shape_info function
def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

# Testing the shape_info function
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)

    print("Circle Info:")
    shape_info(circle)

    print("\nRectangle Info:")
    shape_info(rectangle)

