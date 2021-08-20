def input_control(n):
    res = []
    count = 0
    while count != n:
        cont = int(input('Введите вес контейнера: '))
        if cont > 200 or cont != int(cont):
            print('Неправильный ввод, попробуйте ещё раз сначала')
            res = []
            count = 0
        else:
            res.append(cont)
    return res


n = int(input('Кол-во контейнеров: '))
left_border = []
right_border = []

containers = input_control(n)

new_cont = int(input('\nВведите вес нового контейнера: '))

for cont in containers:
    if cont >= new_cont:
        left_border.append(cont)
    else:
        right_border.append(cont)

containers = left_border + [new_cont] + right_border

if len(left_border) > 0 and len(right_border) > 0:
    print('\nНомер, куда встанет новый контейнер:', len(left_border) + 1)
elif len(left_border) == 0:
    print('\nНомер, куда встанет новый контейнер: 1')
elif len(right_border) == 0:
    print('\nНомер, куда встанет новый контейнер:', len(left_border) + 1)
