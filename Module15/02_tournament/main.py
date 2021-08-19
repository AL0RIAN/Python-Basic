members = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
index = 0

for member in members:
    if index % 2 == 0:
        print(members[index], end=', ')
    index += 1


