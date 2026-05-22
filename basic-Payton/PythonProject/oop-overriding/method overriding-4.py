class shape:

    def area(self):
        print('shape area method ')


class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width


    def area(self):
        rectangle_area = self.length * self.width
        print('rectangle area:', rectangle_area)
        return rectangle_area

class triangle(shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height


class circle(shape):
    PI = 3.14
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        circle_area = self.PI * self.radius * self.radius
        print('circle area:', circle_area)
        return circle_area

shape: list[shape] = [circle(7), rectangle(5, 10), triangle(10, 5)]


for shape in shape:
    shape.area()