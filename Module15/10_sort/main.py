# сортировка пузырьком

n = int(input('Кол-во элементов в списке: '))
origin = []

for _ in range(n):
    number = int(input('Элемент списка: '))
    origin.append(number)

print('Изначальный список:', origin)

for _ in range(len(origin) - 1):
    flag = 0
    for index in range(0, len(origin) - 1):
        if origin[index] > origin[index + 1]:
            a = origin[index]
            b = origin[index + 1]
            origin[index] = b
            origin[index + 1] = a
            flag = 1
    if flag == 0:
        break

print('Отсортированный список:', origin)