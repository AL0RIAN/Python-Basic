s = input('Введите строку: ')
res = []

while s:
    count = 0
    now = s[0]
    for symbol in s:
        if symbol == now:
            count += 1
        else:
            break
    res.extend([now, str(count)])
    s = s[count:]

print('Закодированная строка:', ''.join(res))
