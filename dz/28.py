# class Point:
#     __slots__ = ['__x', '__y', 'z']
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
# # print(p1.__dict__)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_val(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#     def __set_coords_x(self, x):
#         if Point.__check_val(x):
#             self.__x = x
#         else:
#             raise  ValueError("Неверный формат данных")
#         print('Вызов __set_coords_x')
#         self.__x = x
#
#     def __get_coords_x(self):
#         print('Вызов __get_coords_x')
#         return self.__x
#
#     def __del_coords_x(self):
#         print('Удаление свойства')
#         del self.__x
#
#     coordX = property(__get_coords_x, __set_coords_x, __del_coords_x)
#
#
# p1 = Point(5, 10)
# p1.coordX = 100
# print(p1.coordX)
# del p1.coordX
# p1.coordX = 7
# print(p1.coordX)


# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def __check_val(z):
#         if isinstance(z, int) or isinstance(z, float):
#             return True
#         return False
#
#
#     @property
#     def coords_x(self):
#         print('Вызов __get_coords_x')
#         return self.__x
#
#     @coords_x.setter
#     def coords_x(self, x):
#         if Point.__check_val(x):
#             self.__x = x
#         else:
#             raise  ValueError("Неверный формат данных")
#         print('Вызов __set_coords_x')
#         self.__x = x
#
#     @coords_x.deleter
#     def coords_x(self):
#         print('Удаление свойства')
#         del self.__x
#
#
# p1 = Point(5, 10)
# p1.coords_x = 100
# print(p1.coords_x)
# del p1.coords_x
# p1.coords_x = 7
# print(p1.coords_x)


# class KgToPounds:
#     def __init__(self, kg):
#         self.__kg = kg
#
#     @property
#     def kg(self):
#         return self.__kg
#
#     @kg.setter
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             print('Килограммы задаются только числами')
#
#     def to_pounds(self):
#         return self.__kg * 2.205
#
#
# w = KgToPounds(12)
# print(w.to_pounds())
# w.kg = 41
# print(w.kg)
# print(w.to_pounds())


class Point:
   __count = 0

   def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        Point.__count += 1

   @staticmethod
   def get_count(self):
       return Point.__count


p1 = Point()
p1 = Point()
p1 = Point()
#
#
# print(p1.get_count())
# print(Point.get_count())


# class Change:
#     @staticmethod
#     def inc(x):
#         return x + 1
#
#     @staticmethod
#     def dec(x):
#         return x - 1
#
#
# print(Change.inc(10), Change.dec(10))
# q = Change()
# print(q.dec(5), q.inc(5))


# class Numbers:
#     @staticmethod
#     def max(a, b, c, d):
#         if a > b and a > c and a > d:
#             return a
#         if b > a and b > c and b > d:
#             return b
#         if c > b and c > a and c > d:
#             return c
#         if d > b and d > a and d > c:
#             return d
#
#     @staticmethod
#     def min(a, b, c, d):
#         if a < b and a < c and a < d:
#             return a
#         if b < a and b < c and b < d:
#             return b
#         if c < b and c < a and c < d:
#             return c
#         if d < b and d < a and d < c:
#             return d
#
#     @staticmethod
#     def sred(a, b, c, d):
#         return (a + b + c + d)/4
#
#     @staticmethod
#     def factorial(x):
#         fac = 1
#         for i in range(1, x + 1):
#             fac *= i
#         return fac
#
#
#
# print(Numbers.max(1, 2, 3, 4))
# print(Numbers.min(1, 2, 3, 4))
# print(Numbers.sred(1, 2, 3, 4))
# print(Numbers.factorial(4))


# class Date:
#     def __init__(self, day=0, month=0, year=0):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def string_to_db(self):
#         return f'{self.year}-{self.month}-{self.year}'
#
#
# d = '16.12.2021'
# day, month, year = map(int, d.split('.'))
# print(day, month, year)
# date = Date(day, month, year)
# print(date.string_to_db())


class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('.'))
        date1 = cls(day, month, year)
        return date1

    def string_to_db(self):
        return f'{self.year}-{self.month}-{self.year}'


d = Date()
date = d.from_string('16.12.2021')
print(date.string_to_db())
d1 = Date()
date1 = d1.from_string('15.01.2020')
print(date1.string_to_db())