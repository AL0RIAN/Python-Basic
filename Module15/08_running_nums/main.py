n = int(input('Кол-во элементов: '))
origin = []
new = []
k = int(input('Сдвиг: '))

for _ in range(n):
    number = int(input('Элемент списка: '))
    origin.append(number)
for number in range(k, 0, -1):
    new.append(origin[-number])
for number in range(len(origin) - k):
    new.append(origin[number])

print('Изначальный список:', origin)
print('Сдвинутый список:', new)
