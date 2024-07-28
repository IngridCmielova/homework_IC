import math

# Shape
class Shape:
    def calculate_area(self):
        pass

    def __int__(self):
        return int(self.calculate_area())

    def __str__(self):
        return "Tvar: Obecný tvar"

#obdélník
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def __str__(self):
        return f"Obdélník se šířkou {self.width} a výškou {self.height}"

#kruh
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * (self.radius ** 2)

    def __str__(self):
        return f"Kruh s poloměrem {self.radius}"

#pravoúhlý trojúhelník
class RightTriangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

    def __str__(self):
        return f"Pravoúhlý trojúhelník se základnou {self.base} a výškou {self.height}"

# Třída pro lichoběžník
class Trapezoid(Shape):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def calculate_area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

    def __str__(self):
        return f"Lichoběžník se základnami {self.base1}, {self.base2} a výškou {self.height}"

rectangle = Rectangle(10, 5)

print(rectangle)
print(f"Plocha obdélníku: {int(rectangle)}")