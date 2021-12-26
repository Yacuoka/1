#__магическийМетод__

# Специальные методы

# конструктор __new__
# инициализатор __init__
# деструктор __del__


# class Point:
#     count = 0
#
#     # def __new__(cls, *args, **kwargs):
#     #     print('Конструктор')
#     #     return  super().__new__(cls)
#
#
#     def __init__(self, x = 0, y = 0):
#         print('Инициализатор')
#         self.x = x
#         self.y = y
#         Point.count += 1
#
#
#     def check_val(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#
#     def set_coords(self, x, y):
#         if Point.check_val(x) and Point.check_val(y):
#             self.x = x
#             self.y = y
#         else:
#             print('Координаты должны быть числами')
#
#
#     def get_coords(self):
#         return self.x, self.y
#
#
#     def __del__(self):
#         print('Удаление экземпляра: ' + self.__class__.__name__)
#
#
# p1 = Point(5, 10)
# print(p1.__dict__)
# Point.__init__(p1, 20)
# print(p1.__dict__)
# p2 = Point()
# print(p2.__dict__)
# p3 = Point(2)
# print(p3.__dict__)
# del p2
# print(p1.x)
# print(Point.count)
# p1.set_coords(2, 3)
# print(p1.get_coords())


# class Robot:
#     k = 0
#
#
#     def __init__(self, name):
#         self.name = name
#         print('Инициализация робота: ', self.name)
#         Robot.k += 1
#
#
#     def __del__(self):
#         print(self.name, 'выключается!')
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, 'был последним')
#         else:
#             print('Работающих роботов осталось', Robot.k)
#
#
#     def say_hi(self):
#         print('Приветствую! Меня зовут ', self.name)
#
#
#
# droid1 = Robot('R2-D2')
# droid1.say_hi()
# print('Численность роботов: ', Robot.k)
# droid2 = Robot('C-3PO')
# droid2.say_hi()
# print('Численность роботов: ', Robot.k)
#
# print('\nЗдесь роботы могут проделать какую-то работу.\n')
# print("Роботы зкончили свою работу. Давайте выключим.")
# del droid1
# del droid2
#
# print('Численность роботов: ', Robot.k)



class Point:
    WIDTH = 5

    def __init__(self, x, y):
        self.__x = x
        self.__y = y


    def __getattr__(self, item):
        return f'В классе {__class__.__name__} отсутствует атрибут: {item}'

    def __getattribute__(self, item):
        if item == '_Point__x':
            return  'Закрытая переменная'
        else:
            return object.__getattribute__(self, item)

    def __setattr__(self, key, value):
        if key == 'WIDTH':
            raise AttributeError
        else:
            self.__dict__[key] = value

    def area(self):
        return self.__x * self.__y + Point.WIDTH




p1 = Point(5, 10)
print(p1.x, p1.y)
p1.x = 100
p1.y = 'abc'
print(p1.x, p1.y)
print(p1.zzz)
print(p1._Point__x)
print(p1.area())


# Инкапсуляция
# x - Public
# _x - Protected
# __x - Private


# import math
#
# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width
#
#     def set_length(self, length):
#         self.__length = length
#
#
#     def set_width(self, width):
#         self.__width = width
#
#
#     def get_length(self):
#         return self.__length
#
#
#     def get_width(self):
#         return self.__width
#
#
#     def square(self):
#         return self.__length * self.__width
#
#
#     def perimetr(self):
#         return (self.__length + self.__width) * 2
#
#
#     def hypo(self):
#         return math.sqrt(self.__length ** 2 + self.__width ** 2)
#
#
#     def get_draw(self):
#         # for i in range(self.__length):
#         #     print(self.__width * '*')
#         print(self.__width * '*' + '\n' * self.__length)
#
#
# rec1 = Rectangle(3, 9)
# rec1.set_length(3)
# rec1.set_width(9)
# print('Длина прямоугольника: ', rec1.get_length())
# print('Ширина прямоугольника: ', rec1.get_width())
# print('Площадь: ', rec1.square())
# print('Периметр: ', rec1.perimetr())
# print('Гипотенуза: ', round(rec1.hypo()))
# rec1.get_draw()