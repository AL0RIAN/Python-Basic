import random

first = [round(random.uniform(5, 10), 2) for _ in range(20)]
second = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [first[score] if first[score] > second[score] else second[score] for score in range(20)]

print('Первая команда:', first)
print('Вторая команда:', second)
print('Победители:', winners)