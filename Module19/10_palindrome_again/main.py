def palindrome(string):
    char = {}
    for i in string:
        char[i] = char.get(i, 0) + 1

    odd = 0
    for i in char.values():
        if i % 2 != 0:
            odd += 1
    return odd <= 1


text = input('Введите строку: ')

if palindrome(text):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')

# for index in range(1, len(text) + 1):
#     if text == text[::-1]:
#         print('Можно сделать палиндромом')
#         break
#     text = text[-1:] + text[0:-1]
# else:
#     print('Нельзя сделать палиндромом')
