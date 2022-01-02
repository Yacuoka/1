import math

class Pair:
    def __init__(self, A, B):
        self._A = A
        self._B = B

    def edit_A(self, leg1):
        self._A = leg1

    def edit_B(self, leg2):
        self._B = leg2

    def calc_sum(self):
        res = self._A + self._B
        return f'Сумма: {res}'

    def calc_mult(self):
        res = self._A * self._B
        return f'Произведение: {res}'


class Right_Triangle(Pair):
    def __init__(self, A, B):
        super().__init__(A, B)

    def hypotenuse(self):
        C = math.sqrt(self._A ** 2 + self._B ** 2)
        return round(C, 2)

    def C(self):
        hyp = round(math.sqrt(self._A * self._B), 2)
        return f'Гипотенуза: {hyp}'


    def square(self):
        s = 1/2 * (self._A * self._B)
        return f'Площадь: {s}'

    def print_info(self):
        print(f'Прямоугольный треугольник АBС ({self._A},{self._B}, {self.hypotenuse()})')




triang = Right_Triangle(5, 8)
triang.print_info()
print(triang.C())
print(triang.square())
print()
print(triang.calc_sum())
print(triang.calc_mult())
print()
triang.edit_A(10)
triang.edit_B(20)
print(triang.C())
print(triang.calc_sum())
print(triang.calc_mult())
print(triang.square())





