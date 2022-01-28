# class Student:
#     def __init__(self, name, n):
#         self.name = name
#         self.note = n
#
#     def show(self):
#         print(self.name)
#         self.note.show()
#
#     class Laptop:
#         def __init__(self, model, cpu, memory):
#             self.model = 'HP'
#             self.cpu = 'i7'
#             self.memory = 16
#
#         def show(self):
#             print(f" => {self.model}, {self.cpu}, {self.memory}")
#
#
# s3 = Student.Laptop('HP', 'i7', 16)
# s1 = Student('Roman', s3)
# s2 = Student('Vladimir', s3)
# s1.show()
# s2.show()


#Mixins / Примеси

# class Displayer:
#     @staticmethod
#     def display(message):
#         print(message)
#
# class LoggerMixin:
#     def log(self, message, filename='logfile.txt'):
#         with open(filename, 'a') as fh:
#             fh.write(message)
#
#     def display(self, message):
#         Displayer.display(message)
#         self.log(message)
#
#
# class MySubClass(LoggerMixin, Displayer):
#     def log(self, message, filename=''):
#         super().log(message, filename='subclasslog.txt')
#
#
# sub = MySubClass()
# sub.display('Это строка будет отображаться и записываться в файл')


# class Goods:
#     def __init__(self, name, weight, price):
#         super().__init__()
#         print('Init Goods')
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def print_inform(self):
#         print(f'{self.name}, {self.weight}, {self.price}')
#
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         print('Init MixinLog')
#         self.ID += 1
#         self.id = self.ID
#
#     def save_sell_log(self):
#         print(f'{self.id}: товар был продан в 00:00 часов')
#
#
# class Notebook(Goods, MixinLog):
#     pass
#
#
# n = Notebook('HP', 1.5, 35000)
# n.print_inform()
# n.save_sell_log()


#Перегрузка операторов

class Clock:
    __DAY = 86400 #24 * 60 * 60

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError('Секунды должны быть целым числом')

        self.__secs = secs % self.__DAY

    def get_format_time(self):
        s = self.__secs % 60 # секунды
        m = (self.__secs // 60) % 60 # минуты
        h = (self.__secs // 3600) % 24 # часы
        return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else '0' + str(x)

    def __add__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')
        return Clock(self.__secs + other.__secs)

    def __sub__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError('Правый операнд должен быть типом Clock')

            return Clock(self.__secs - other.__secs)

    def __eq__(self, other):
        return self.__secs == other.__secs
        # if self.__secs == other.__secs:
        #     return True
        # return False

    def __ne__(self, other):
        return not self.__eq__(other)


c1 =Clock(100)
c2 =Clock(200)
c3 = Clock(300)
print(c1.get_format_time())
print(c2.get_format_time())
c3 = c1 + c2
print(c3.get_format_time())
print('c2 - c3', c3.get_format_time())

if c1 == c2:
    print('Впемя одинаковое')
else:
    print('Время разное')
