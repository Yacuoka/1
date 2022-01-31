class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_perimetr(self):
        return 2 * (self.w * self.h)


class Square:
    def __init__(self, a):
        self.a = a

    def get_perimetr(self):
        return 4 * self.a


r1 = Rectangle(1, 2)
r2 = Rectangle(2, 4)
s1 = Square(10)
s2 = Square(20)

shape = [r1, r2, s1, s2]

for g in shape:
        print(g.get_perimetr())
