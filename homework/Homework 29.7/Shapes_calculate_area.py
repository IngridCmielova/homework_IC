class Shape:
    def __init__(self):
        pass

    def calculate_area(self):
        pass

#obdelnik
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

#kruh
import math

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

#pravouhly trojuhelnik
class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.heigh

#Lichobeznik
class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def calculate_area(self):
        return 0.5 * (self.base1 + self.base2) * self.height