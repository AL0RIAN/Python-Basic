text = input('Введите строку: ')

for index in range(1, len(text) + 1):
    if text == text[::-1]:
        print('Можно сделать палиндромом')
        break
    text = text[-1:] + text[0:-1]
else:
    print('Нельзя сделать палиндромом')

