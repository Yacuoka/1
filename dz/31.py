# import re
#
#
# class UserDate:
#     def __init__(self, fio, old, ps, weight):
#         # self.verify_fio(fio)
#         # self.verify_old(old)
#         self.verify_weight(weight)
#         self.verify_ps(ps)
#
#         self.fio = fio
#         self.old = old
#         self.__password = ps
#         self.__weight = weight
#
#     @classmethod
#     def verify_fio(cls, fio):
#         if not isinstance(fio, str):
#             raise TypeError('ФИО должно быть строкой')
#         f = fio.split()
#         if len(f) != 3:
#             raise TypeError('Неверный формат ФИО')
#         letters = ''.join(re.findall(r'[a-zа-яё-]', fio, flags=re.IGNORECASE))
#         for s in f:
#             if len(s.strip(letters)) != 0:
#                 raise TypeError('В ФИО можно использовать только буквы и дефисы')
#
#
#     @classmethod
#     def verify_old(cls, old):
#         if not isinstance(old, int) or old < 14 or old > 100:
#             raise TypeError('Возраст должен быть числом в диапазоне от 14 до 100 лет')
#
#     @classmethod
#     def verify_weight(cls, w):
#         if not isinstance(w, (int, float)) or w < 20:
#             raise TypeError('Вес должен быть числом от 20 кг и выше')
#
#     @classmethod
#     def verify_ps(cls, ps):
#             if not isinstance(ps, str):
#                 raise TypeError('Паспорт должен быть строкой')
#             s = ps.split()
#             if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
#                 raise TypeError('Неверный формат паспорта')
#
#     @property
#     def fio(self):
#         return self.__fio
#
#     @fio.setter
#     def fio(self, fio):
#         self.verify_fio(fio)
#         self.__fio = fio
#
#     @property
#     def old(self):
#         return self.__old
#
#     @old.setter
#     def fio(self, old):
#         self.verify_old(old)
#         self.__old = old
#
#     @property
#     def password(self):
#         return self.__password
#
#     @password.setter
#     def password(self, ps):
#         self.verify_ps(ps)
#         self.__password = ps
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.verify_weight()
#         self.__weight = weight
#
#
# p1 = UserDate('Решетова Екатерина Викторовна', 26, '1234 567890', 80.8)
# p1.fio = 'Соболев Игорь Николаевич'
# p1.weight = 60
# print(p1.__dict__)


from abc import ABC, abstractmethod


# абстрактный класс
class Chess(ABC):
    def draw(self):
        print('Нарисовал шахматную фигуру')

    @abstractmethod
    def move(self): # абстрактный метод
        pass


class Queen(Chess):
    def move(self):
        print('Ферзь перемещен на е4')


q = Queen()
q.draw()
q.move


from math import pi

# class Table:
#
#     def __init__(self, width=None, length=None, radius=None):
#         if radius is None:
#             self._width = width
#             self._length = length
#         else:
#             self._radius = radius
#
#     def set_radius(self, radius):
#         self._radius = radius
#
#     def set_sides(self, width=None, length=None):
#         if length is None:
#             self._width = self._length = width
#         else:
#             self._width = width
#             self._length = length
#
#     def calc_area(self):
#         raise NotImplementedError('В дочернем классе должен быть определен метод calc_area()')
#
#
# class Sq_table(Table):
#     def calc_area(self):
#         return self._width * self._length
#
# class Round_table(Table):
#     def calc_area(self):
#         return pi + self._radius ** 2
#
#
# t = Sq_table(20, 10)
# print(t.__dict__)
# print(t.calc_area())
#
# t1 = Round_table(radius=10)
# print(t.__dict__)
# print(t.calc_area())