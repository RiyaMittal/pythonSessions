from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):

    type = "RectangLe"

    def __init__(self):
        self.length = 10
        self.breath = 11

    # def printarea(self):
    #     return self.length * self.breath
    #

rect = Rectangle()
