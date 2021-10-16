n = int(input('Кол-во палок: '))
k = int(input('Кол-во бросков: '))

sticks = ['I' for _ in range(n)]

for throw in range(k):
    left = int(input('Граница слева: ')) - 1
    right = int(input('Граница справа: '))
    count = right - left
    print('\nБросок ' + str(throw + 1) + '. Cбиты палки с номера', left + 1, 'по номер', right)
    sticks[left:right] = '.' * count

print('\nРезультат:', end=' ')
for i in sticks:
    print(i, end='')
