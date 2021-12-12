def pro_sum(data, suma=0):
    if not isinstance(data, list) and not isinstance(data, tuple):
        return data
    for value in data:
        if isinstance(value, list) or isinstance(value, tuple):
            suma += pro_sum(value)
        else:
            suma += value
    return suma


print('pro_sum([[1, 2, [3]], [1], 3])')
print('Ответ: ', pro_sum([[1, 2, [3]], [1], 3]))
print('pro_sum((1, 2, 3, 4, 5)')
print('Ответ: ', pro_sum((1, 2, 3, 4, 5)))
