def list_to_text(lst):
    for symbol in lst:
        print(symbol, end='')
    print()


text = list(input('Введите строку: '))
left = text.index('h')
right = len(text[left:]) - 1  # TODO не верный способ, надо найти позицию второй буквы h

print('Было:', end=' '), list_to_text(text)
text[left + 1:right] = text[left + 1:right][::-1]
print('Стало:', end=' '), list_to_text(text)
