shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name = input('Название детали: ')
count = 0
cost = 0

for i in shop:  # TODO Используйте распаковку списка: for name, price in shop:
    if i[0] == name:
        count += 1
        cost += i[1]

print('Кол-во деталей -', count)
print('Общая стоимость -', cost)