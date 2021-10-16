answer = 0
с_rolls = int(input('Кол-во коньков: '))
rolls = []

for i in range(с_rolls):
    print('Размер', i + 1, 'пары: ', end='')
    n = int(input())
    rolls.append(n)

print()

с_people = int(input('Кол-во людей: '))
people = []
for i in range(с_people):
    print('Размер ноги', i + 1, 'человека: ', end='')
    n = int(input())
    people.append(n)

for roll in rolls:
    for size in people:
        if size <= roll:
            people.remove(size)
            answer += 1

print('Наибольшее кол-во людей, которые могут взять ролики:', answer)
