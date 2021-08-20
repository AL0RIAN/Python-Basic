n = int(input('Кол-во контейнеров: '))
left_border = []
right_border = []
containers = []

while len(containers) != n:
    for _ in range(n):
        if len(containers) == n:
            break
        cont = int(input('Введите вес контейнера: '))
        if cont > 200 or cont != int(cont):
            print('Неверный ввод - попробуйте сначала')
            containers = []
        else:
            containers.append(cont)

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
