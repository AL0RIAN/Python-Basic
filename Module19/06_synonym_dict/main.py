def checker(dictionary):
    check = input('Введите слово: ').lower()
    if check in result:
        print('Синоним: {}'.format(result[check].capitalize()))
    elif check in result.values():
        for key in dictionary:
            if dictionary[key] == check:
                print('Синоним: {}'.format(key.capitalize()))
    else:
        print('Такого слова в словаре нет. Попробуйте ещё раз')
        checker(dictionary)


n = int(input('Кол-во пар: '))
result = dict()

for index in range(n):
    print(index + 1, 'пара:', end=' ')
    word = input().lower().split(' - ')
    result.setdefault(word[0], word[1])
print()

for _ in range(n):
    checker(result)
