# class Power:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __call__(self, func):
#         def wrapper(a, b):
#             res = func(a, b)
#             return res ** self.arg
#             print(res)
#
#         return wrapper
#
#
# @Power(3)
# def multiple(a, b):
#     return a * b
#
#
# print('Результат: ', multiple(2, 2))


# def dec(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 20)
#         fn(*args, **kwargs)
#         print("*" * 20)
#     return wrap
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     @dec
#     def info(self):
#         print(f'{self.name} {self.surname}')
#
#
# p1 = Person('Виталий', 'Карасёв')
# p1.info()


# def decorator(cls):
#     class Wrapper(cls):
#         def doubler(self, value):
#             return value * 2
#
#     return Wrapper
#
# @decorator
# class ActualClass:
#     def __init__(self):
#         print('Init ActualClass:')
#
#     def quad(self, value):
#         return value * 4
#
#
# obj = ActualClass()
#
# print(obj.quad(4))
# print(obj.doubler(4))


# class Message:
#     _REGISTERY = {}
#
#     def __init__(self, text):
#         self.text = text
#
#     @classmethod
#     def register(cls, name):
#         def decorator(klass):
#             cls._REGISTERY[name] = klass
#             return klass
#
#         return decorator
#
#     @classmethod
#     def create(cls, message_type, text):
#         klass = cls._REGISTERY.get(message_type)
#         if klass is None:
#             raise ValueError('Такого мессенджера нет.')
#         print(text, end=' ')
#         return klass(text)
#
#
# @Message.register('Telegram')
# class Telegram(Message):
#     def send(self):
#         print('(Telegram)')
#
# @Message.register('WhatsApp')
# class WhatsApp(Message):
#     def send(self):
#         print('(WhatsApp)')
#
#
# m1 = Telegram.create('Telegram', 'text')
# m1.send()
# m2 = WhatsApp.create('WhatsApp', 'new text')
# m2.send()


#Дескриптор

# class Person:
#     def __init__(self, name, surname):
#         self.__name = name
#         self.__surname = surname
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, value):
#         self.__name = value
#
#     @property
#     def surname(self):
#         return self.__surname
#
#     @surname.setter
#     def surname(self, value):
#         self.__surname = value
#
#
# p = Person('Иван', 'Николаев')


# class String:
#     def __init__(self, value=None):
#         if value:
#             self.set(value)
#
#     def set(self, value):
#         self.__value = value
#
#     def get(self):
#         return self.__value
#
#
# class Person:
#     def __init__(self, name, surname):
#         self.name = String(name)
#         self.surname = String(surname)
#
#
# p = Person('Иван', 'Николаев')
# print(p.name.get())
# p.name.set('Игорь')
# print(p.name.get())


# __get__()
# __set__()
# __delete__()
# __set_name__()


# class ValidString:
#     def __set_name__(self, owner, name):
#         self.__name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.__name]
#
#     def __set__(self, instance, value):
#         if not isinstance(value, str):
#             raise ValueError(f'{self.__name} должно быть строкой')
#         instance.__dict__[self.__name] = value
#
#
# class Person:
#     name = ValidString()
#     surname = ValidString()
#
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# p = Person('Иван', 'Николаев')
# print(p.name)
# p.name = 'Игорь'
# print(p.name)
# print(p.surname)


# data descriptor
class NonNegative:
    def __set_name__(self, owner, name):
         self.__name = name

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Значение должно быть положительным')
        instance.__dict__[self.__name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]


class Order:
    price = NonNegative()
    quantity = NonNegative()

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total(self):
        return self.price * self.quantity


apple = Order('apple', 5, 10)
print(apple.total())
