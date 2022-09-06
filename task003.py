# 3.Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).
#
# *Пример:*
#
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

def quarter_number(num_x, num_y):
    if num_x == 0 and num_y ==0:
        print('Точка находится в начале координат')
    elif num_x == 0:
        print('Точка находится на оси X')
    elif num_y == 0:
        print('Точка находится на оси Y')
    elif num_x > 0 and num_y > 0:
        print('Точка находится в I четверти')
    elif num_x < 0 and num_y > 0:
        print('Точка находится в II четверти')
    elif num_x < 0 and num_y < 0:
        print('Точка находится в III четверти')
    elif num_x > 0 and num_y < 0:
        print('Точка находится в IV четверти')


x = float(input('Введите X: '))
y = float(input('Введите Y: '))
quarter_number(x, y)
