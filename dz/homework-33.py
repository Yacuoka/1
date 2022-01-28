class Clock:
    __DAY = 86400

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError('Секунды должны быть целым числом')

        self.__secs = secs % self.__DAY

    def get_format_time(self):
        s = self.__secs % 60
        m = (self.__secs // 60) % 60
        h = (self.__secs // 3600) % 24
        return f'{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}'

    @staticmethod
    def __get_form(x):
        return str(x) if x > 9 else '0' + str(x)

    def __gt__(self, other):
        return self.__secs > other.__secs

    def __lt__(self, other):
        return self.__secs < other.__secs

    def __le__(self, other):
        return self.__secs <= other.__secs

    def __ge__(self, other):
        return self.__secs >= other.__secs


c1 = Clock(100)
c2 = Clock(200)
c3 = Clock(300)

if c3 > c2:
    print('c3 > c2')
else:
    print('c3 < c2')


if c3 < c2:
    print('c2 < c3')
else:
    print('c2 > c3')


if c3 <= c2:
    print('c3 =< c2')
else:
    print('c2 =< c3')


if c3 >= c2:
    print('c3 >= c2')
else:
    print('c2 >= c3')