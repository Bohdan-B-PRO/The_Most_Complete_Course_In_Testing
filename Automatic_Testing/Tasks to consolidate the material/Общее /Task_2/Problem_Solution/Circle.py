import math


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = math.pi * self.radius**2
        return area

    def get_circumference(self):
        l = 2 * (math.pi * self.radius)
        return l










