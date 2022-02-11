#Создание модулей

# import math
# print(math.pi)
#
# from math import pi
# print(pi)


# from Geometry import rect, sq, trian
# from Geometry import *
# from Geometry import trian
#
#


# def main():
    # t1 = Triangle(1, 2, 3)
    # t2 = Triangle(4, 5, 6)
    #
    # shape = [t1, t2]
    #
    # for g in shape:
    #     print(g.get_perimeter())


# if name == '__main__':
#     main()


from car import electrocar


def main():

    e = electrocar.ElectroCar('Tesla', 'T', 2018, 99000)
    e.show_car()
    e.description_battery()


if __name__ == '__main__':
    main()




