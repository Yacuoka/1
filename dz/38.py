# Упаковка данных

# Сериализация (кодирование) - запись данных на диск
# Десериализация (декодирование) - чтение данных из памяти/с диска


# Три модуля в страндартной библиотеке Python:
# - marshal
# - pickle
# - json

#  dump() - сохраняет данные в файл
# load() - считывает данные из файла

#  dumps() - сохраняет данные в оперативную память
# loads() - считывает данные из оперативной памяти

# import pickle

# filename = 'basket.txt'
#
# shop_list = {
#     'фрукты': ['яблоки', 'манго'],
#     'овощи': ['морковь'],
#     'бюджет': 1000
# }
#
# with open(filename, 'wb') as fh:
#     pickle.dump(shop_list, fh)
#
# with open(filename, 'rb') as fh:
#     print(pickle.load(fh))


# class Test:
#     a_number = 35
#     a_string = 'привет'
#     a_list = [1, 2, 3]
#     a_tuple = (22, 23)
#     a_dict = {'first': 'a', 'second': 2, 'third': [1, 2, 3]}
#
#     def __str__(self):
#         return f'Число: {Test.a_number}\nСтрока: {Test.a_string}\nСписок: {Test.a_list}\nКортеж: {Test.a_tuple}\nСловарь: {Test.a_dict}'
#
#
#
# obj = Test()
#
# my_obj = pickle.dumps(obj)
# print(f'Сериализация в строку:\n{my_obj}\n')
#
# l_obj = pickle.loads(my_obj)
# print(f'Десериализация в строку:\n{l_obj}\n')


# class Test2:
#     def __init__(self):
#         self.a = 35
#         self.b = 'test'
#         self.c = lambda x: x * x
#
#     def __str__(self):
#         return f'{self.a} {self.b} {self.c(2)}'
#
#     def __getstate__(self):
#         attr = self.__dict__.copy()
#         print(attr)
#         del attr['c']
#         print(attr)
#         return attr
#
#     def __setstate__(self, state):
#         self.__dict__ =  state
#         self.c = lambda x: x * x
#         print(state)
#
#
# item1 = Test2()
# item2 = pickle.dumps(item1)
# item3 = pickle.loads(item2)
# print(item3.__dict__)
# print(item3)


# class TextReader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.file = open(filename, encoding='utf-8')
#         self.count = 0
#
#     def read_line(self):
#         self.count += 1
#         line = self.file.readline()
#         if not line:
#             return None
#         if line.endswith('\n'):
#             line = line[:-1]
#         return f'{self.count}: {line}'
#
#     def __getstate__(self):
#         state = self.__dict__.copy()
#         del state['file']
#         return state
#
#     def __setstate__(self, state):
#         self.__dict__.update(state)
#         file = open(self.filename, encoding='utf-8')
#         for i in range(self.count):
#             file.readline()
#         self.file = file
#
#
#
# reader = TextReader('hello.txt')
# print(reader.read_line())
# print(reader.read_line())
#
# new_reader = pickle.loads(pickle.dumps(reader))
# print(new_reader.read_line())


import json

# data = {
#     'FirstName': 'Jane',
#     'LastName': 'Djo',
#     'Hobbies': ('running', 'sky diving'),
#     'Age': 5
# }

# with open('data_file.json', 'w') as fw:
#     json.dump(data, fw, indent=4)
#
# with open('data_file.json', 'r') as fw:
#     print(json.load(fw))


# st = json.dumps(data, sort_keys=True)
#
# data = json.loads(st)
# print(data)


# x = {
#     'name': 'Виктор'
# }
# y = {
#     'name': 'Виктор'
# }
#
# print(json.dumps(x))
# print(json.dumps(y, ensure_ascii=False))


from random import choice


# def get_person():
#     name = ''
#     tel = ''
#
#     letters = ['a', 'b', 'd', 'e', 'f', 'e', 'g']
#     num = ['1', '2', '3', '4', '6', '8', '9', '0']
#
#     while len(name) != 7:
#         name += choice(letters)
#     print(name)
#
#     while len(tel) != 10:
#         tel += choice(num)
#     print(tel)
#
#
# get_person()


def get_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'd', 'e', 'f', 'e', 'g']
    num = ['1', '2', '3', '4', '6', '8', '9', '0']

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(num)

    person = {
        'name': name,
        'tel': tel
    }

    return person


def write_json(person_dict):
    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = []

    data.append(person_dict)
    with open('persons.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

for i in range(5):
   write_json(get_person())


# with open('persons.json', 'a') as f:
#     json.dump(persons, f, indent=2, ensure_ascii=False)