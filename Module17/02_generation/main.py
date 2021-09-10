n = int(input('Длина списка: '))

generation = [1 if index % 2 == 0 else index % 5 for index in range(n)]
print('Результат:', generation)
