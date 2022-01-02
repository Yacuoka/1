# class Figure:
#     def __init__(self, color):
#         self.__color = color
#
#     @property
#     def color(self):
#         return self.__color
#
#     @color.setter
#     def color(self, c):
#         self.__color = c
#
#
#
# class Rectangle(Figure):
#     def __init__(self, width, height, color, border):
#         super().__init__(color)
#         self.__width = width
#         self.__height = height
#         self.border = border
#
#     @property
#     def width(self):
#         return self.__width
#
#     @width.setter
#     def width(self, w):
#         if w > 0:
#             self.__width = w
#         else:
#             raise ValueError('Значение ширины должно быть больше нуля!')
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, h):
#         if h > 0:
#             self.__height = h
#         else:
#             raise ValueError('Значение высоты должно быть больше нуля!')
#
#     def border_new(self):
#         return self.border
#
#     def area(self):
#         # return self.color
#         return self.__width * self.__height
#         # return self.border_new()
#
#
#
# rect = Rectangle(10, 20, 'green', '1px solid grey')
# print(rect.area())
# print(rect.width)
# print(rect.height)
# print(rect.color)
# print(rect.border)
# rect.width = 50
# print(rect.width)
# print(rect.area())


class Liquid:
    def __init__(self, name, density):
        self._name = name
        self._density = density

    def edit_density(self, val):
        self._density = val

    def calc_v(self, m):
        res = m / self._density
        print(f'Объём {m} кг {self._name} равен {res} m^3')
        return res

    def calc_m(self, v):
        res = v * self._density
        print(f'Вес {v} m^3 {self._name} составляет {res} кг')
        return res

    def print_info(self):
        print(f'Жидкость {self._name}, плотность - {self._density} kg/m^3')


class Alcohol(Liquid):
    def __init__(self, name, density, strength):
        super().__init__(name, density)
        self.strength = strength

    def edit_strength(self, val):
        self.strength = val

a = Alcohol('Wine', 1064.2, 14)
a.print_info()
a.edit_density(1000)
a.print_info()

a.calc_v(0.5)
a.calc_m(0.5)

print(a.strength)
a.edit_strength(20)
print(a.strength)