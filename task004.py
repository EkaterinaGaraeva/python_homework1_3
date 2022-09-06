# 4.Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y)

def coordinates(number):
    match number:
        case 1:
            print(f'{number} четверть => X > 0, Y > 0')
        case 2:
            print(f'{number} четверть => X < 0, Y > 0')
        case 3:
            print(f'{number} четверть => X < 0, Y < 0')
        case 4:
            print(f'{number} четверть => X > 0, Y < 0')


n = int(input('Введите номер четверти: '))
coordinates(n)
