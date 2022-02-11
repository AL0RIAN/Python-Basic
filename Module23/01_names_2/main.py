def count_letter(word, num):
    res = 0
    try:
        for sym in word:
            if sym != '\n':
                res += 1
        if res < 3:
            raise Exception(f'Ошибка в {num + 1} строке')
    except Exception as error:
        print(error)
    finally:
        return res


n = int(input('Введите кол-во имён: '))
with open('people.txt', 'w') as file:
    for line in range(n):
        name = input(f'{line + 1} имя: ') + '\n'
        file.write(name)


result = 0
temp = 0
number = 0

with open('people.txt', 'r') as file:
    while number < 3:
        for line in file.readlines():
            result += count_letter(line, number)
            number += 1
print('Ответ:', result)
