from math import *
from Shape import rectangle
from Shape import circle

class Cylinder(circle.Circle, rectangle.Rectangle):
    def __init__(self, r, h):
        super().__init__(r)
        super().__init__(h)
        self.h = h

    def get_cylinder_volume(self):
        return self.r ** 2 * pi * self.h


__author__ = 'Ekaterina'
if __name__ == '__main__':
    print(f'Module {__name__} (author: {__author__})')