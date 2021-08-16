def reverse_float(number):
    switcher = 0
    res1 = ''
    res2 = ''
    for symbol in str(number):
        if symbol == '.':
            switcher = 1
        elif switcher == 0:
            res1 = symbol + res1
        else:
            res2 = symbol + res2
    return float(res1 + '.' + res2)


n = float(input('Введите первое число: '))
k = float(input('Введите второе число: '))
print('\nПервое число наоборот:', reverse_float(n))
print('Второе число наоборот:', reverse_float(k))
