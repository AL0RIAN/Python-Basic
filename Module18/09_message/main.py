message = input('Сообщение: ').split()
res = []

for word in message:
    alpha = ''
    new_word = ''
    for symbol in word:
        if symbol.isalpha():
            alpha = symbol + alpha
        else:
            new_word += alpha + symbol
            alpha = ''
    new_word += alpha
    res.append(new_word)

print('Новое сообщение:', ' '.join(res))
