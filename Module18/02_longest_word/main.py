text = input('Строка: ')
res = ['', 0]
print(text)

for word in text.split():
    if len(word) > res[1]:
        res[1] = len(word)
        res[0] = word

print('\nСамое длинное слово - {0}, а его длина {1}!'.format(res[0], res[1]))
