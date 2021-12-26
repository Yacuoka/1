class Temperature:
    __count = 0

    def __init__(self):
        Temperature.__count += 1

    @staticmethod
    def get_count():
        return Temperature.__count

    @staticmethod
    def CeltoFar(Celsius):
        if isinstance(Celsius, (int, float)):
            return Celsius * 9 / 5 + 32
        else:
            return 'Температура задаётся числовым значением'

    @staticmethod
    def FartoCel(Fahrenheit):
        if isinstance(Fahrenheit, (int, float)):
            return (Fahrenheit - 32) / 1.8
        else:
            return 'Температура задаётся числовым значением'


t1 = Temperature()
print(t1.CeltoFar(0))
t2 = Temperature()
print(t2.FartoCel(32))
print(Temperature.get_count())
