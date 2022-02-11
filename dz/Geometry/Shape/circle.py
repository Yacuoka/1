from math import *

class Circle:
    def __init__(self, r):
        self.r = r

    def get_circle_length(self):
        return self.r * 2 * pi
        res = print(f'Длина: {res}')
        return res

    def get_circle_square(self):
        return self.r ** 2 * pi
        res = print(f'Площадь: {res}')
        return res

    def print_circle(self):
        print(f'Радиус: {self.r}')


__author__ = 'Ekaterina'
if __name__ == '__main__':
    print(f'Module {__name__} (author: {__author__})')

