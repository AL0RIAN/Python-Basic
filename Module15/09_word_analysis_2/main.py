word = list(input('Слово: '))
reverse_word = []

for index in range(1, len(word) + 1):
    reverse_word.append(word[-index])

if reverse_word == word:
    print('\nСлово является палиндромом')
else:
    print('\nСлово не является палиндромом')
