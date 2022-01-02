# class Account:
#     rate_usd = 0.013
#     rate_euro = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_euro = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname # фамилия владельца
#         self.num = num # номер счёта
#         self.percent = percent # процент начисления
#         self.value = value # сумма в рублях
#         print(f'Счёт #{self.num}, принадлежащий {self.surname}, был открыт.')
#         print('*' * 50)
#
#     def __del__(self):
#         print('*' * 50)
#         print(f'Счёт #{self.num}, принадлежащий {self.surname}, был закрыт.')
#
#
#     @classmethod
#     def set_usd_rate(cls, rate): # редактирование курса рубля по отношению к доллару
#          cls.rate_usd = rate
#
#     @classmethod
#     def set_euro_rate(cls, rate): # редактирование курса рубля по отношению к евро
#          cls.rate_euro = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def edit_owner(self, surname): # смена владельца счёта
#         self.surname = surname
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print('Проценты были успешно начислены!')
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f'У вас нет {val} {Account.suffix}')
#         else:
#             self.value -= val
#             print(f'{val} {Account.suffix} было успешно снято')
#             self.print_balance()
#
#     def add_money(self, val):
#         self.value += val
#         print(f'{val} {Account.suffix} было успешно добавлено')
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f'Состояние счёта: {usd_val} {Account.suffix_usd}')
#
#     def convert_to_euro(self):
#         euro_val = Account.convert(self.value, Account.rate_euro)
#         print(f'Состояние счёта: {euro_val} {Account.suffix_euro}')
#
#     def print_balance(self):
#         print(f'Текущий баланс: {self.value} {Account.suffix}')
#
#     def print_info(self): # вывод информации о счёте
#         print('Информация о счёте')
#         print('-' * 20)
#         print(f'#{self.num}')
#         print(f'Владелец: {self.surname}')
#         self.print_balance()
#         print(f'Проценты: {self.percent: .0%}')
#         print('-' * 20)
#
#
#
# acc = Account('Долгих', 12345, 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_euro()
# print()
#
# Account.set_usd_rate(2)
# acc.convert_to_usd()
#
# Account.set_euro_rate(1.5)
# acc.convert_to_euro()
# print()
# acc.edit_owner('Дюма')
# acc.print_info()
# print()
# acc.add_percent()
# print()
# acc.withdraw_money(3000)
# acc.withdraw_money(200)
# print()
# acc.add_money(5000)
# acc.withdraw_money(3000)



# Наследование (Базоваый класс - Дочерний класс)

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        # return f'{self.x}, {self.y}'
        a = str(self.x), str(self.y)
        return a



print(issubclass(Point, object))

class Prop:
    def __init__(self, sp:Point, ep:Point, color:str ='red', width:int =1):
     print('Инициализатор базового класса Prop')
     self.sp = sp
     self.ep = ep
     self.color = color
     self.__width = width

    def get_width(self):
        return self.__width

class Line(Prop):
    def __init__(self, *args):
        print('Переопределённый инициали затор Line')
        super().__init__(*args)

    def draw_line(self):
        print(f'Рисование линии: {self.sp}, {self.ep}, {self.color}, {self.get_width}')


line = Line(Point(1, 2, Point(10, 20)))
print(line.__dict__)
line.width = 10
print(line.width)
line.draw_line()