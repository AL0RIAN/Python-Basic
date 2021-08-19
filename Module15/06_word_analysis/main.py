word = input('Введите слово: ')
lit_list = []
exceptions = []

for sym in word:
    c = 0
    for i in word:
        if sym == i:
            c += 1
        if c >= 2:
            exceptions.append(sym)

for sym in word:
    if sym not in exceptions:
        lit_list.append(sym)

print('Кол-во уникальных букв:', len(lit_list))
