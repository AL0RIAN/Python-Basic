def circle_destroyer(m):
    for _ in range(k):
        if m == len(circle) - 1:
            m = 0
        else:
            m += 1
    print('Выбывает человек под номером', circle[m])
    circle.remove(circle[m])


n = int(input('Кол-во человек: '))
k = int(input('Какое число в считалке? '))
circle = list(range(1, n + 1))
print('Значит, выбывает каждый', k, 'человек')

while len(circle) > 1:
    print('\nТекущий круг людей:', circle)
    member = int(input('Начало счёта с номера: '))
    member = circle.index(member) - 1
    circle_destroyer(member)

print('\nОстался человек под номером', circle[0])
