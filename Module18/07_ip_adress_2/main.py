ip = input('\nВведите IP: ').split('.')
for symbol in ip:
    if len(ip) < 4:
        print('Адрес - это четыре числа, разделенные точками')
        break
    elif not symbol.isdigit():
        print('{} - не целое число'.format(symbol))
        break
    elif int(symbol) > 255:
        print('{} превышает 255'.format(symbol))
        break
else:
    print('IP-адрес корректен')

