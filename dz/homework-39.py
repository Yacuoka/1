import json

class Country:
    def __init__(self, country):
        self.country = country

    def __str__(self):
        return f'Справочник: {self.country}'

    def add_country(self):
        key = input('Введите страну для добавления: ')
        value = input('Введите столицу: ')
        self.country[key] = value
        x = list(value)
        return self.value

    def delete_country(self):
        key = input('Введите страну для удаления: ')
        self.country.pop(key)
        return self.country

    def edit_country(self):
        key = input('Введите страну для редактирования: ')
        if key in self.country:
            print(f'Столица {self.country[key]}, страна {key}')
        else:
            print('Такой страны нет в словаре!')
            self.country[key] = edit
            print('Cтрана добавлена в словарь')

    def search_country(self):
        key = input('Введите страну для поиска: ')
        if key in self.country:
            print(f'Столица {self.country[key]}, страна {key}')
        else:
            print('Такой страны нет в словаре!')


    @classmethod
    def dump_to_json(cls, country, filename):
        try:
            data = json.load(open(filename))
        except FileNotFoundError:
            data = {}
            
    

    @classmethod
    def load_from_file(cls, filename):
        with open(filename, 'r') as f:
            print(json.load(f))


count_dict = {'Россия', 'Москва',
              'Китай', 'Пекин',
              'Германия', 'Берлин',
              'США', 'Вашингтон',
              'Велиткобритания', 'Лондон'
}

g = Country(count_dict)
print('Выберите действие')

while True:
    enter = input('Ввод действия: ')
    if enter == '1':
        g.add_country()
    elif enter == '2':
        g.delete_country()
    elif enter == '3':
        g.edit_country()
    elif enter == '4':
        g.search_country()


    else:
        print('Такой функции нет')


c1 = Country('Россия', 'Москва')
c2 = Country('Китай', 'Пекин')
c3 = Country('Германия', 'Берлин')
c4 = Country('США', 'Вашингтон')
c5 = Country('Велиткобритания', 'Лондон')

Country.dump_to_json(с1, 'countries.json')
Country.load_from_file('countries.json')

g.add_country()
g.search_country()
print(c1)
print(c1)
Country.delete_country(3)
print(c1)
# Country.edit_couintry(2, 4)
# print(c1)
