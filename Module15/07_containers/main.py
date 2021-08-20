n = int(input('Кол-во контейнеров: '))
containers = []
left_border = []
right_border = []

for _ in range(n):
    cont = int(input('Введите вес контейнера: '))
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