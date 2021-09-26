n = int(input('Введите максимальное число: '))
result = {'right': set()}  # TODO почему множество пустое?

while True:
    numbers = input('\nНужное число есть среди вот этих чисел: ').lower()
    if numbers == 'помогите!':
        break
    yesNo = input('Ответ Артёма: ').lower()
    lst = [int(number) for number in numbers.split()]
    if yesNo == 'да':
        result['right'] = result['right'] | set(lst)  # TODO нужно пересечение множеств, а не объединение
    elif yesNo == 'нет':
        result['right'] = result['right'] - set(lst)
    else:
        print('Неверный ввод')

print('\nАртём мог загадать следующие числа: ', end='')
for number in result['right']:
    print(number, end=' ')
