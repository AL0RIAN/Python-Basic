n = int(input('Сколько клеток: '))
cells = []

print('Кол-во клеток:', n)

for i in range(n):
    print('Эффективность', i + 1, 'клетки: ', end='')
    cell = int(input())
    cells.append(cell)

for index in range(n):
    if cells[index] < index:
        print('\nНеподходящие значения:', cells[index], end=' ')
