# class Human:
#     def __init__(self, last_name, first_name, age):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.age = age
#
#     def info(self):
#         print(f'{self.last_name} {self.first_name} {self.age}')
#
#
# class Student(Human):
#     def __init__(self, speciality, group, rating, last_name, first_name, age):
#         super().__init__(last_name, first_name, age)
#         self.speciality = speciality
#         self.group = group
#         self.rating = rating
#
#     def info(self):
#         print(f'{self.speciality} {self.group} {self.rating}', end=' ')
#         super().info()
#
#
# class Teacher(Human):
#     def __init__(self, speciality, experience, last_name, first_name, age):
#         super().__init__(last_name, first_name, age)
#         self.speciality = speciality
#         self.experience = experience
#
#     def info(self):
#         print(f'{self.speciality} {self.experience}', end=' ')
#         super().info()
#
#
# class Graduate(Student):
#     def __init__(self, topic, speciality, group, rating, last_name, first_name, age):
#         super().__init__(speciality, group, rating, last_name, first_name, age)
#         self.topic = topic
#
#     def info(self):
#         print(f'{self.topic}', end=' ')
#         super().info()
#
#
# group = [
#     Student('Батодалаев', 'Даши', 16, 'ГК', 'Web_011', 5),
#     Graduate('Шугани', 'Сергей', 15, 'РПО', 'PD_011', 5, 'Защита персональных данных'),
#     Teacher('Башкиров', 'Алексей', 45, 'Разработка приложений', 20)
#
# ]
#
# for i in group:
#     i.info()

#
# class Point:
#     def __init__(self, *args):
#         self.__coords = args
#
#     def __len__(self):
#         return len(self.__coords)
#
#     def __abs__(self):
#         return list(map(abs, self.__coords))
#
#     def __str__(self):
#         print(f'{self.__coords}')
#
#
# p = Point(6, -9, 2)
# print(len(p))
# print(p.__dict__)
# print(abs(p))
# print(dir(Point))
# print(p)


# import math
#
#
# class Point:
#     __slots__ = ('x', 'y', 'length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.length = math.sqrt(x * x + y * y)
#
#
# p = Point(5, 9)
# print(p.length)


# class Point:
#     __slots__ = ('x', 'y', 'length')
#
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# class Point2D(Point):
#     __slots__ = 'z',
#
#     def __init__(self, x, y, z):
#         super().__init__(x, y)
#         self.z = z
#
#
# pt2 = Point2D(10, 20)
# pt2.z = 30
# print(pt2.z)


# Функтеры


# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     def __call__(self, *args, **kwargs):
#         self.__counter += 1
#         print(self.__counter)
#         return self.__counter
#
#
# c1 = Counter()
# c1()
# c1()
# c2 = Counter()
# c2()


# class StripsChars:
#     def __init__(self, chars):
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise ValueError('Арумент должен быть строкой')
#         return args[0].strip(self.__chars)
#
#
# s1 = StripsChars('?.!,$ ')
# print(s1(' ?Hello World! '))
#
#
# def strip_string(chars):
#     def wrap(string):
#         if not isinstance(string, str):
#             raise ValueError('Арумент должен быть строкой')
#         return string.strip(chars)
#     return wrap
#
#
# s1 = StripsChars('?.!,$ ')
# print(s1(' ?Hello World! '))

