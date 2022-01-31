from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def print_figure(self):
        pass

    @abstractmethod
    def print_info(self):
        pass


class Square(Shape):
    def __init__(self, side, color):
        self.side = side
        super().__init__(color)

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

    def print_info(self):
        print(f'===Квадрат===\nСторона: {self.side}\nЦвет: {self.color}\nПлощадь: {self.area()}\nПериметр: {self.perimeter()}\n')
        self.print_figure()

    def print_figure(self):
        print((('*' * self.side) + '\n') * self.side)


class Rectangle(Shape):
    def __init__(self, side1, side2, color):
        self.side1 = side1
        self.side2 = side2
        super().__init__(color)

    def perimeter(self):
        return 2 * (self.side1 + self.side2)

    def area(self):
        return self.side1 * self.side2

    def print_info(self):
        print(f'===Прямоугольник===\nДлина: {self.side1}\nШирина: {self.side2}\nЦвет: {self.color}\nПлощадь: {self.area()}\nПериметр: {self.perimeter()}\n')
        self.print_figure()

    def print_figure(self):
        print((('*' * self.side2) + '\n') * self.side1)


class Triangle(Shape):
    def __init__(self, side1, side2, side3, color):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        super().__init__(color)

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        return round(0.5 * self.side1 * ((self.side2 ** 2 - (0.5 * self.side1) ** 2) ** 0.5), 2)

    def print_info(self):
        print(f'===Треугольник===\nСторона 1: {self.side1}\nСторона 2: {self.side2}\nСторона 3: {self.side3}\nЦвет: {self.color}\nПлощадь: {self.area()}\nПериметр: {self.perimeter()}\n')
        self.print_figure()

    def print_figure(self):
            for i in range(self.side2):
                print(' ' * (self.side1 // 2 - i) + '*' * i + '*' + '*' * i + '\n', end='')


f1 = Square(3, 'red')
f2 = Rectangle(3, 7, 'green')
f3 = Triangle(11, 6, 6, 'yellow')


for i in (f1, f2, f3):
    i.print_info()
