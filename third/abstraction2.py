import math
import numbers

from abc import ABC, abstractmethod

# import abc

"""
abc: module name (built in module)
ABC: Abstract class in abc module
abstractmethod: annotations that can be given to abstract methods
"""


class Volume(ABC):

    @abstractmethod
    def volume(self):
        pass


class Shape(ABC):

    def __init__(self):
        self.name = type(self).__name__

    @abstractmethod
    def area(self) -> numbers:
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Square(Shape):

    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self) -> numbers:
        return self.side * self.side


class Circle(Shape):

    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area(self) -> numbers:
        return math.pow(self.radius) * math.pi


class Rectangle(Shape):

    def __init__(self, width, length):
        super().__init__()
        self.width = width
        self.length = length

    def area(self) -> numbers:
        return self.width * self.length


class Cube(Shape, Volume):

    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self) -> numbers:
        return 6 * (self.side ** 2)

    def volume(self):
        return self.side ** 3


class Cylinder(Shape, Volume):

    def __init__(self, radius, height):
        super().__init__()
        self.radius = radius
        self.height = height

    def area(self) -> numbers:
        return 2 * math.pi * self.radius *(self.radius + self.height)

    def volume(self):
        return math.pi * (self.radius ** 2) * self.height


square1 = Square(5)

print(square1)
print(square1.area())

rectangle1 = Rectangle(3, 7)
print(rectangle1)
print(rectangle1.area())

print('_________________________')
cube1 = Cube(5)
print(f'Cube area is => {cube1.area()}')
print(f'Cube volume is => {cube1.volume()}')
print('_________________________')

print('_________________________')
cylinder1 = Cylinder(5, 7)
print(f'Cylinder area is => {cylinder1.area()}')
print(f'Cylinder volume is => {cylinder1.volume()}')
print('_________________________')
