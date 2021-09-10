alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
text = input('Введите текст: ')
shift = int(input('Введите сдвиг: '))

res = [alphabet[(alphabet.index(symbol) + shift) % 33] if symbol in alphabet else symbol for symbol in text]

print('Шифр Цезаря:', end=' ')
for symbol in res:
    print(symbol, end='')

# res = [alphabet[alphabet.index(symbol) + shift] if alphabet.index(symbol) + shift <= len(alphabet) - 1 else alphabet[
#     alphabet.index(symbol) + shift - len(alphabet)] for symbol in text]
