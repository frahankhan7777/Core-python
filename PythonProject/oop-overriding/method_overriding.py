class shape:
    def area(self):
        print("shape area>>>>")
        return print("shape class area method")


class rectangle(shape):
    def area(self):
        print("rectangel area>>>>")
        return print("rectangel area method")



r = rectangle()
r.area()

s =shape()
s.area()

shape: shape = rectangle()
shape.area()
