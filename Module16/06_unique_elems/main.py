first = []
second = []
for _ in range(3):
    number = int(input('Целое число в первый список: '))
    first.append(number)
print()

for _ in range(7):
    number = int(input('Целое число во второй список: '))
    second.append(number)

print('\nПервый список:', first)
print('Второй список:', second)
first.extend(second)

for number in first:
    for _ in range(first.count(number) - 1):
        first.remove(number)

print('\nНовый первый список с уникальными элементами:', first)
