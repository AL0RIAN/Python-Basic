text = input('Текст: ').split()

for index in range(len(text)):
    text[index] = text[index].capitalize()
print(' '.join(text))

