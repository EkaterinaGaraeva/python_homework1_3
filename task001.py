# 1.Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.
#
# *Пример:*
#
# - 6 -> да
# - 7 -> да
# - 1 -> нет

def day_of_week(number):
    match number:
        case 1:
            print('Понедельник, будний день')
        case 2:
            print('Вторник, будний день')
        case 3:
            print('Среда, будний день')
        case 4:
            print('Четверг, будний день')
        case 5:
            print('Пятница, будний день')
        case 6:
            print('Суббота, выходной день')
        case 7:
            print('Воскресенье, выходной день')


n = int(input('Введите число: '))
day_of_week(n)
