# 2.Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

def truth_check():
    # left = 0
    # right = 0
    for x in True, False:
        for y in True, False:
            for z in True, False:
                # left = not(x or y or z)
                # right = not x and not y and not z
                if not(x or y or z) == (not x and not y and not z):
                    print(f'x = {x}, y = {y}, z = {z} => Истинно')
                else:
                    print(f'x = {x}, y = {y}, z = {z} => Ложно')


truth_check()
