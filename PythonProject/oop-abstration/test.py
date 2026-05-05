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
        rectangle_area = self.length  * self.width
        print("rectangle area:", rectangle_area)
        return rectangle_area


r = rectangle(5, 10)
r.area()