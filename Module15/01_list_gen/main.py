n = int(input('Целое число: '))

odd = []

for number in range(1, n):
    if number % 2 != 0:
        odd.append(number)

print('Итог:', odd)
