import random

suma = 0

with open('lucky.txt', 'w') as lucky_file:
    while suma < 777:
        number = input('Введите число: ')
        chance = random.randint(1, 13)
        try:
            if chance == 1:
                raise Exception
            else:
                lucky_file.write(number + '\n')
                suma += int(number)
        except Exception:
            print('Вас постигла неудача!')
            break
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
