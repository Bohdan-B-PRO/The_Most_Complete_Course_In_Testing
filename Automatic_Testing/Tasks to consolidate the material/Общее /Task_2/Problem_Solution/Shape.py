import math


class Shape:

    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        pass


class Circle(Shape):

    def calculate_area(self):
        self.area = math.pi * self.radius ** 2
        return self.area


class Rectangle(Shape):

    def __init__(self, length, width):
        super().__init__(length)
        self.width = width

    def calculate_area(self):
        self.area = self.radius * self.width
        return self.area


circle = Circle(5)
print(f"Circle Area: {circle.calculate_area()}")

rectangle = Rectangle(4, 6)
print(f"Rectangle Area: {rectangle.calculate_area()}")
