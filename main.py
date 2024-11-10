import math
#task1,2
class Figure:
    def area(self):
        raise NotImplementedError("This method must be defined.")
    def __int__(self):
        return int(self.area())
    def __str__(self):
        return "Figure"
class Rectangle(Figure):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def __str__(self):
        return f"Rectangle with length {self.length} and width {self.width}. Area: {self.area()}"
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2
    def __str__(self):
        return f"Circle with radius {self.radius}. Area: {self.area()}"
class RightTirangle(Figure):
    def __init__(self, leg_triangle, leg2_triangle):
        self.leg_triangle = leg_triangle
        self.leg2_triangle = leg2_triangle
    def area(self):
        return 0.5 * self.leg_triangle * self.leg2_triangle
    def __str__(self):
        return f"RightTriangle with legs {self.leg1} and {self.leg2}. Area: {self.area()}"
class Trapezoid(Figure):
    def __init__(self, bases_trapezium, bases2_trapezium, height):
        self.bases_trapezium = bases_trapezium
        self.bases2_trapezium = bases2_trapezium
        self.height = height
    def area(self):
        return 0.5 * (self.bases_trapezium + self.bases2_trapezium) * self.height
    def __str__(self):
        return f"Trapezoid with bases {self.base1} and {self.base2} and height {self.height}. Area: {self.area()}"

circle1 = Circle(5)
print(int(circle1))
print(circle1)
