main = [1, 5, 3]
first = [1, 5, 1, 5]
second = [1, 3, 1, 5, 3, 3]

main.extend(first)
print('Кол-во пятерок в основном списке, слитом с первым побочным:', main.count(5))

while 5 in main:
    main.remove(5)

main.extend(second)
print('Кол-во троек в основном списке, слитом со вторым побочным:', main.count(3))
print('Итоговый список:', main)

