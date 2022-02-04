class Person:
    def __init__(self, surname, name, age):
        self.surname = surname
        self.name = name
        self.age = age

    @property
    def data(self):
        return self.surname, self.name, self.age

    def __str__(self):
        return f'{self.surname}, {self.name}, {self.age}'


class SortKey:
    def __init__(self, *args):
        self.__method = args

    def __call__(self, lst):
        lst.sort(key=lambda j: [j.__dict__[key] for key in self.__method])


p = [Person('Иванов', 'Игорь', 21), Person('Петров', 'Степан', 25), Person('Сидоров', 'Антон', 28),
     Person('Петров', 'Анатолий', 11), Person('Иванов', 'Иван', 28)]

for i in p:
    print(i.data)
print()

s1 = SortKey('surname')
s1(p)
for i in p:
    print(i.data)
print()

s2 = SortKey('surname', 'name')
s2(p)
for i in p:
    print(i.data)



