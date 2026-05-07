from time import sleep


class shape:
    def execute(self):
        if self.validate():
            self.area()

        else:
            print("validate failed")

    def validate(self):
        return False

    def area(self):
            print("shape area met")
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def validate(self):
        if self.length > 0 and self.width > 0:
            return True
        else:
            return  False

    def area(self):
        rectangle_area = self.length * self.width
        print("rectangle area:", rectangle_area)
        return rectangle_area


class circle(shape):
    PI = 3.14


    def __init__(self, radius):
        self.radius = radius

    def validate(self):
        if self.radius > 0:
            return True
        else:
            return  False

    def area(self):
        circle_area =  self.PI * self.radius * self.radius
        print("circle area :", circle_area)
        return  circle_area

class text(shape):
    pass

print("/n--- rectangle---")
r = rectangle(10, 20)
r.execute()

print("/n--- circle---")
c = circle(10)
c.execute()

print("/n---invalide rectangle0---")
r_invalid = rectangle(-5, 10)
r_invalid.execute()


print("/n --- test---")
t = text()
t.execute()