from abc import ABC, abstractmethod


class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(shape):
    def  __init__(self, radius):
        self.radius = radius

def area(self):
    return 3.14 * self.radius * self.radius

class Square(shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length  * self.length

circle_1 = Circle