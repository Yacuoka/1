class NonFloat:
    def __set_name__(self, owner, name):
         self.__name = name

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('Значение должно быть целочисленным')
        instance.__dict__[self.__name] = value

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]


class Point3D:
    x = NonFloat()
    y = NonFloat()
    z = NonFloat()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def coords(self):
        return {'_x': self.x, '_y': self.y, '_z': self.z}


p = Point3D(1, 2, 3)
print(p.coords())