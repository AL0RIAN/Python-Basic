n = int(input('Кол-во заказов: '))
result = dict()

for index in range(n):
    print(index + 1, 'заказ:', end=' ')
    order = input().split()
    if order[0] not in result.keys():
        result[order[0]] = {order[1]: int(order[2])}
    elif order[1] in result[order[0]]:
        result[order[0]][order[1]] += int(order[2])
    else:
        result[order[0]].update({order[1]: int(order[2])})

for key1 in sorted(result.keys()):
    print('{}:'.format(key1))
    for key2 in result[key1]:
        print('{0}{1}: {2}'.format(' ' * 7, key2, result[key1].get(key2)))
