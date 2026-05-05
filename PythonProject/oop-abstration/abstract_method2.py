from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass


class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


r = rectangle(9,6)
print("area of rectangle:", r.area())


shape:shape = rectangle(5, 10)
print("area of ractangle (using shpae reference ) :", shape.area())