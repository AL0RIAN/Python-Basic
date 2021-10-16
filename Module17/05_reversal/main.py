def list_to_text(lst):
    for symbol in lst:
        print(symbol, end='')
    print()


text = (input('Введите строку: '))
left = text.index('h')
right = text.rindex('h')
text = list(text)

print('Было:', end=' '), list_to_text(text)
text[left + 1:right] = text[left + 1:right][::-1]
print('Стало:', end=' '), list_to_text(text)
