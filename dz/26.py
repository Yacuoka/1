# class Point:
#     """Класс для предоставления кооординат точек на плоскости"""
#     x = 1
#     y = 1
#
#
#     def set_coords(self, x, y):
#         self.x = x
#         self.y = y
#         print('Координаты')
#
#
# p1 = Point()
# Point.x = 100
# p1.y = 5
# p1.z = 20
# print(p1.x, Point.y, p1.y)
# print(p1.__dict__)
# print(Point.__dict__)
# print(getattr(p1, 'x'))
# print(hasattr(p1, 'x'))
# print(hasattr(p1, 'z'))
# setattr(p1, 'a', 7)
# print(p1.__dict__)
# delattr(p1, 'a')
# print(isinstance(p1, Point))
# p1.set_coords(5, 10)
# print(p1.__dict__)
#
# p2 = Point()
# p2.set_coords(40, 80)
# print(p2.__dict__)
# print(Point.__doc__)
# print(Point.__name__)
# print(dir(Point))


# class Human:
#     name = 'name'
#     birthday = '00.00.0000'
#     phone = '00-00-00'
#     country = 'country'
#     city = 'city'
#     adress = 'Street, house'
#
#
#     def print_info(self):
#         print(' Персональные данные: '.center(40, '*'))
#         print(f'Имя: {self.name}\nДата рождения: {self.birthday}\nДата рождения: {self.phone}\nСтрана: {self.country}\nГород: {self.city}\nДомашний адрес: {self.adress}')
#         print('=' * 40)
#
#
#     def input_info(self, first_name, birthday, phone, country, city, adress):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.adress = adress
#
#     def set_name(self, name):
#         self.name = name
#
#     def get_name(self):
#         return self.name
#
#     def set_birthday(self, birthday):
#         self.birthday = birthday
#
#     def get_birthday(self):
#         return self.birthday
#
#     def set_phone(self, phone):
#         self.phone = phone
#
#     def get_phone(self):
#         return self.phone
#
#     def set_country(self, country):
#         self.country = country
#
#     def get_county(self, country):
#         return self.country
#
#     def set_city(self, city):
#         self.city = city
#
#     def get_city(self, city):
#         return self.city
#
#     def set_adress(self, adress):
#         self.adress = adress
#
#     def get_city(self, adress):
#         return self.adress
#
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info('Юлия', '23.05.1986', '45-46-98', 'Россия', 'Москва', 'Чистопрудный бульвар, 1A')
# h1.print_info()
# h1.set_name('Ирина')
# h1.print_info()
# h1.get_name()
# h1.set_birthday('15.07.2002')
# h1.get_birthday()
# h1.set_phone('066-47-74')
# h1.get_phone()
# h1.set_country('Грузия')
# h1.get_country()
# h1.set_city('Тбилиси')
# h1.get_city()
# h1.set_city('Шота Руставели, 1')
# h1.get_city()


class Car:
    name = 'name'
    year = '0000'
    model = 'model'
    power = '000 л. с.'
    colour  = 'colour'
    price = '0$'


    def print_info(self):
        print("Данные автомобиля".center(20, '*'))
        print(f'Название модели: {self.name}\nГод выпуска: {self.year}\nПроизводитель: {self.model}\nМощность двигателя: {self.power}\nЦвет: {self.colour}\nЦена: {self.price}')
        print('*'*40)


    def input_info(self, name, year, model, power, colour, price):
        self.name = name
        self.year = year
        self.model = model
        self.power = power
        self.colour = colour
        self.price = price


    def set_model(self, model):
        self.model = model


    def get_model(self):
        return self.model


car1 = Car()
car1.print_info()
car1.input_info('X7 M501', '2020', 'BMW', '530 л.с.', 'white', '100000$')
car1. print_info()
car1. set_model('Lada')
car1.print_info()
print(car1.get_model())


# class Person:
#     skill = 10
#
#     def print_info(self, name, surname):
#         self.name = name
#         self.surname = surname
#         print(f'Данные сотрудника: {self.name} {self.surname}')
#
#
#     def add_skill(self, k):
#         self.skill += k
#         print('Квалификация сотрудника: ', self.skill)
#
#
# p1 = Person()
# p1.print_info('Виктор', 'Резник')
# p1.add_skill(3)
# print()
# p2 = Person()
# p2.print_info('Анна', 'Долгих')
# p2.add_skill(2)


def sum_arg(a, b):
    print(a + b)

sum_arg(5, 2)
sum_arg('Hello', 'world')