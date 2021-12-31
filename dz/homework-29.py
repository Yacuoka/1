# Вариант 1
class Account:
    rate_usd = 0.013
    rate_euro = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_euro = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.__surname = surname # фамилия владельца
        self.__num = num # номер счёта
        self.__percent = percent # процент начисления
        self.__value = value # сумма в рублях
        print(f'Счёт #{self.__num}, принадлежащий {self.__surname}, был открыт.')
        print('*' * 50)

    def set_surname(self, surname):
        self.__surname = surname

    def set_num(self, num):
        self.__num = num

    def set_percent(self, percent):
        self.__percent = percent

    def set_value(self, value):
        self.__value = value

    def get_surname(self):
        return self.__surname

    def get_num(self):
        return self.__num

    def get_percent(self):
        return self.__percent

    def get_value(self):
        return self.__value

    def __del__(self):
        print('*' * 50)
        print(f'Счёт #{self.__num}, принадлежащий {self.__surname}, был закрыт.')


    @classmethod
    def set_usd_rate(cls, rate): # редактирование курса рубля по отношению к доллару
         cls.rate_usd = rate

    @classmethod
    def set_euro_rate(cls, rate): # редактирование курса рубля по отношению к евро
         cls.rate_euro = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def edit_owner(self, surname): # смена владельца счёта
        self.__surname = surname

    def add_percent(self):
        self.__value += self.__value * self.__percent
        print('Проценты были успешно начислены!')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f'У вас нет {val} {Account.suffix}')
        else:
            self.__value -= val
            print(f'{val} {Account.suffix} было успешно снято')
            self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f'{val} {Account.suffix} было успешно добавлено')

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f'Состояние счёта: {usd_val} {Account.suffix_usd}')

    def convert_to_euro(self):
        euro_val = Account.convert(self.__value, Account.rate_euro)
        print(f'Состояние счёта: {euro_val} {Account.suffix_euro}')

    def print_balance(self):
        print(f'Текущий баланс: {self.__value} {Account.suffix}')

    def print_info(self): # вывод информации о счёте
        print('Информация о счёте')
        print('-' * 20)
        print(f'#{self.__num}')
        print(f'Владелец: {self.__surname}')
        self.print_balance()
        print(f'Проценты: {self.__percent: .0%}')
        print('-' * 20)

acc = Account('Долгих', 12345, 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_euro()
print()

Account.set_usd_rate(2)
acc.convert_to_usd()

Account.set_euro_rate(1.5)
acc.convert_to_euro()
print()
acc.edit_owner('Дюма')
acc.print_info()
print()
acc.add_percent()
print()
acc.withdraw_money(3000)
acc.withdraw_money(200)
print()
acc.add_money(5000)
acc.withdraw_money(3000)
print()


# Вариант 2
class Account:
    rate_usd = 0.013
    rate_euro = 0.011
    suffix = 'RUB'
    suffix_usd = 'USD'
    suffix_euro = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.__surname = surname # фамилия владельца
        self.__num = num # номер счёта
        self.__percent = percent # процент начисления
        self.__value = value # сумма в рублях
        print(f'Счёт #{self.__num}, принадлежащий {self.__surname}, был открыт.')
        print('*' * 50)

        @property
        def surname(self):
            return self.__surname

        @surname.setter
        def surname(self, surname):
            self.__surname = surname

        @property
        def num(self):
            return self.__num

        @num.setter
        def num(self, num):
            self.__num = num

        @property
        def percent(self):
            return self.__percent

        @percent.setter
        def percent(self, percent):
            self.__percent = percent

        @property
        def value(self):
            return self.__value

        @value.setter
        def value(self, value):
            self.__value = value

    def __del__(self):
        print('*' * 50)
        print(f'Счёт #{self.__num}, принадлежащий {self.__surname}, был закрыт.')


    @classmethod
    def set_usd_rate(cls, rate): # редактирование курса рубля по отношению к доллару
         cls.rate_usd = rate

    @classmethod
    def set_euro_rate(cls, rate): # редактирование курса рубля по отношению к евро
         cls.rate_euro = rate

    @staticmethod
    def convert(value, rate):
        return value * rate

    def edit_owner(self, surname): # смена владельца счёта
        self.__surname = surname

    def add_percent(self):
        self.__value += self.__value * self.__percent
        print('Проценты были успешно начислены!')
        self.print_balance()

    def withdraw_money(self, val):
        if val > self.__value:
            print(f'У вас нет {val} {Account.suffix}')
        else:
            self.__value -= val
            print(f'{val} {Account.suffix} было успешно снято')
            self.print_balance()

    def add_money(self, val):
        self.__value += val
        print(f'{val} {Account.suffix} было успешно добавлено')

    def convert_to_usd(self):
        usd_val = Account.convert(self.__value, Account.rate_usd)
        print(f'Состояние счёта: {usd_val} {Account.suffix_usd}')

    def convert_to_euro(self):
        euro_val = Account.convert(self.__value, Account.rate_euro)
        print(f'Состояние счёта: {euro_val} {Account.suffix_euro}')

    def print_balance(self):
        print(f'Текущий баланс: {self.__value} {Account.suffix}')

    def print_info(self): # вывод информации о счёте
        print('Информация о счёте')
        print('-' * 20)
        print(f'#{self.__num}')
        print(f'Владелец: {self.__surname}')
        self.print_balance()
        print(f'Проценты: {self.__percent: .0%}')
        print('-' * 20)



acc = Account('Долгих', 12345, 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_euro()
print()

Account.set_usd_rate(2)
acc.convert_to_usd()

Account.set_euro_rate(1.5)
acc.convert_to_euro()
print()
acc.edit_owner('Дюма')
acc.print_info()
print()
acc.add_percent()
print()
acc.withdraw_money(3000)
acc.withdraw_money(200)
print()
acc.add_money(5000)
acc.withdraw_money(3000)