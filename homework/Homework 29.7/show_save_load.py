class Shape:
    def show(self):
        raise NotImplementedError("Tato metoda musí být implementována v podtřídě.")

    def save(self, filename):
        # Uložení tvaru do souboru
        with open(filename, 'a') as f:
            f.write(self.__str__() + "\n")

    def __str__(self):
        return "Obecný tvar"


class Square(Shape):
    def __init__(self, x, y, side_length):
        self.x = x
        self.y = y
        self.side_length = side_length

    def show(self):
        print(f"Čtverec s levým horním rohem na ({self.x}, {self.y}) a délkou strany {self.side_length}")

    def __str__(self):
        return f"Čtverec {self.x} {self.y} {self.side_length}"


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Obdélník s levým horním rohem na ({self.x}, {self.y}), šířka {self.width}, výška {self.height}")

    def __str__(self):
        return f"Obdélník {self.x} {self.y} {self.width} {self.height}"


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def show(self):
        print(f"Kruh se středem na ({self.x}, {self.y}) a poloměrem {self.radius}")

    def __str__(self):
        return f"Kruh {self.x} {self.y} {self.radius}"


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def show(self):
        print(f"Elipsa s levým horním rohem opsaného obdélníku na ({self.x}, {self.y}), šířka {self.width}, výška {self.height}")

    def __str__(self):
        return f"Elipsa {self.x} {self.y} {self.width} {self.height}"


# Vytvoření seznamu tvarů
shapes = [
    Square(1, 2, 5),
    Rectangle(3, 4, 6, 7),
    Circle(5, 6, 3),
    Ellipse(7, 8, 9, 4)
]

# Uložení tvarů do souboru
for shape in shapes:
    shape.save('shapes.txt')

# Načtení tvarů ze souboru a jejich zobrazení
with open('shapes.txt', 'r') as f:
    for line in f:
        print(line.strip())