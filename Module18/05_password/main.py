while True:
    password = input('Придумайте пароль: ')
    up = 0
    digit = 0
    for symbol in password:
        if symbol.isupper():
            up += 1
        if symbol.isdigit():
            digit += 1
    if len(password) >= 8 and digit >= 3 and up >= 1:
        print('Это надежный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')


