import math
#task1
class Figure:
    def area(self):
        raise NotImplementedError("This method must be defined.")
class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
class RightTirangle(Figure):
    def __init__(self, leg_triangle, leg2_triangle):
        self.leg_triangle = leg_triangle
        self.leg2_triangle = leg2_triangle
    def area(self):
        return 0.5 * self.leg_triangle * self.leg2_triangle
class Trapezoid(Figure):
    def __init__(self, bases_trapezium, bases2_trapezium, height):
        self.bases_trapezium = bases_trapezium
        self.bases2_trapezium = bases2_trapezium
        self.height = height
    def area(self):
        return 0.5 * (self.bases_trapezium + self.bases2_trapezium) * self.height

circle1= Circle(5)
print(circle1.area())
