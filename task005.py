# 5.Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# *Пример:*
#
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

import math

def find_distance(xa, ya, xb, yb):
    ab = round(math.sqrt((xb-xa)**2+(yb-ya)**2), 2)
    return ab


xA = float(input('Введите координату X точки A: '))
yA = float(input('Введите координату Y точки A: '))
xB = float(input('Введите координату X точки B: '))
yB = float(input('Введите координату Y точки B: '))
print(f'Расстояние между точками А({xA};{yA}) и В({xB};{yB}) = {find_distance(xA, yA, xB, yB)}')
