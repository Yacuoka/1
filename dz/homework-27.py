import math


class Sphere:
    def __init__(self, radius=0.6, x=0, y=0, z=0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_center(self):
        return self.x, self.y, self.z

    def get_volume(self):
        return (self.radius ** 3) * math.pi * 4 / 3

    def get_square(self):
        return (self.radius ** 2) * math.pi * 4

    def is_point_inside(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        if (self.x) ** 2 + (self.y) ** 2 + (self.z) ** 2 < self.radius ** 2:
            return True
        return False


sp1 = Sphere()
sp1.get_radius()
print('Радиус: ', sp1.get_radius())
print('Объём: ', sp1.get_volume())
print('Площадь шара: ', sp1.get_square())
print('Координаты центра: ', tuple(sp1.get_center()))
print(sp1.is_point_inside(0, -1.5, 0))
sp1.set_radius(1.6)
print(sp1.is_point_inside(0, -1.5, 0))
