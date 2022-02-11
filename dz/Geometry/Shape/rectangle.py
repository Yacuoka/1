class Rectangle:
    def __init__(self, l, h):
        self.l = l
        self.h = h

    def get_rect_perimeter(self):
        return 2 * (self.l + self.h)
        res = print(f'Периметр: {res}')
        return res

    def get_rect_area(self):
        return self.l * self.h
        res = print(f'Площадь: {res}')
        return res

    def print_rect(self):
        print(f'Стороны: {self.l}, {self.h}')


__author__ = 'Ekaterina'
if __name__ == '__main__':
    print(f'Module {__name__} (author: {__author__})')