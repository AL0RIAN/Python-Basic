members = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
index = 0

for member in members:
    if index % 2 == 0:
        print(members[index], end=', ')  # TODO member содержит именно то, что в members[index] :)
    index += 1

# TODO другой вариант - итерировать по индексам с шагом 2, тогда if не понадобится
