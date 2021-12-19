class Book:
    name = 'name'
    release = '0000'
    publisher = 'publisher'
    genre = 'genre'
    author = 'author'
    price = '0$'


    def print_info(self):
        print(' Данные об издании: '.center(40, '*'))
        print(
            f'Название: {self.name}\nГод выпуска: {self.release}\nИздатель: {self.publisher}\nЖанр: {self.genre}\nАвтор: {self.author}\nЦена: {self.price}')
        print('=' * 40)

    def input_info(self, name, release, publisher, genre, author, price):
        self.name = name
        self.release = release
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def set_name(self, name):
        self.name = name

    def get_name(self, name):
        return self.name

    def set_release(self, release):
        self.release = release

    def get_release(self, release):
        return self.release

    def set_publisher(self, publisher):
        self.publisher = publisher

    def get_publisher(self, publisher):
        return self.publisher

    def set_genre(self, genre):
        self.genre = genre

    def get_genre(self, genre):
        return self.genre

    def set_author(self, author):
        self.author = author

    def get_author(self, author):
        return self.author

    def set_price(self, price):
        self.price = price

    def get_price(self, price):
        return self.price


obj = Book()
obj.print_info()
obj.input_info('"История государства Российского"', '2009', '"Эксмо"', 'История России', 'Н. М. Карамзин', '15$')
obj.print_info()
obj.set_name('"Северная Корея: вчера и сегодня"')
obj.set_release('1995')
obj.set_publisher('"Восточная литература"')
obj.set_genre('Путешествия')
obj.set_author('А. Н. Ланьков')
obj.set_price('10$')
obj.print_info()