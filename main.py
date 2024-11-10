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

#task3
class Shape:
    def show(self):
        raise NotImplementedError("This method must be implemented in subclasses.")
    @staticmethod
    def save(filename, shapes):
        with open(filename, "w") as file:
            for shape in shapes:
                file.write(shape.to_text() + '\n')
    @staticmethod
    def load(filename):
        shapes = []
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split(', ')
                shape_type = data[0]
                if shape_type == "Square":
                    shapes.append(Square(int(data[1]), int(data[2]), int(data[3])))
                elif shape_type == "Rectangle":
                    shapes.append(Rectangle(int(data[1]), int(data[2]), int(data[3]), int(data[4])))
                elif shape_type == "Circle":
                    shapes.append(Circle(int(data[1]), int(data[2]), int(data[3])))
                elif shape_type == "Ellipse":
                    shapes.append(Ellipse(int(data[1]), int(data[2]), int(data[3]), int(data[4])))
        return shapes
class Square(Shape):
    def __init__(self, x, y, side):
        self.type = "Square"
        self.x = x
        self.y = y
        self.side = side
    def show(self):
        return f"Square with top-left corner at ({self.x}, {self.y}) and side length {self.side}"
    def to_text(self):
        return f"Square, {self.x}, {self.y}, {self.side}"
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.type = "Rectangle"
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def show(self):
        return f"Rectangle with top-left corner at ({self.x}, {self.y}), width {self.width}, and height {self.height}"
    def to_text(self):
        return f"Rectangle, {self.x}, {self.y}, {self.width}, {self.height}"
class Circle(Shape):
    def __init__(self, x, y, radius):
        self.type = "Circle"
        self.x = x
        self.y = y
        self.radius = radius
    def show(self):
        return f"Circle with center at ({self.x}, {self.y}) and radius {self.radius}"
    def to_text(self):
        return f"Circle, {self.x}, {self.y}, {self.radius}"
class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.type = "Ellipse"
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def show(self):
        return f"Ellipse with top-left corner at ({self.x}, {self.y}), width {self.width}, and height {self.height}"
    def to_text(self):
        return f"Ellipse, {self.x}, {self.y}, {self.width}, {self.height}"
shapes = [
    Square(1, 2, 5),
    Rectangle(0, 0, 10, 4),
    Circle(3, 3, 7),
    Ellipse(2, 2, 6, 4)
]
Shape.save("shapes.txt", shapes)
loaded_shapes = Shape.load("shapes.txt")
for shape in loaded_shapes:
    print(shape.show())