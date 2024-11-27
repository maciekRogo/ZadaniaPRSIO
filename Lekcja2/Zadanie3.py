"""Stwórz klasy Rectangle i Circle , które będą miały wspólną metodę area() . Klasa
Rectangle powinna obliczać pole prostokąta, a klasa Circle – pole koła. Następnie napisz
funkcję calculate_area , która przyjmie listę obiektów tych klas i wywoła metodę area()
na każdym z nich, bez względu na to, czy obiekt jest prostokątem, czy kołem."""
class Shape:
    def area(self):
        raise NotImplementedError("Ta metoda musi być zaimplementowana")
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * (self.radius ** 2)
def calculate_area(shapes):
    for shape in shapes:
        print(shape.area())
shapes = [Rectangle(2, 3), Circle(2)]
calculate_area(shapes)