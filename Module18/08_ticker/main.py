first = input('Первая строка: ')
second = input('Вторая строка: ')

for index in range(len(first)):
    if first[-index::] + first[:-index] == second:
        print('Первая строка получается из второй со сдвигом:', index)
        break
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига')
