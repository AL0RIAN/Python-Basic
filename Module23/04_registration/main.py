def correct(data):
    try:
        error = ''
        if len(data) != 3:
            error += 'IndexError: НЕ присутствуют все три поля: '
            raise IndexError
        elif not data[0].isalpha():
            error += 'NameError: Поле имени содержит НЕ только буквы'
            raise NameError
        elif not ('@' in data[1] and '.' in data[1]):
            error += 'SyntaxError: Поле емейл НЕ содержит @ и .(точку)'
            raise SyntaxError
        elif not (10 <= int(data[2]) < 99):
            error += 'ValueError: Поле возраст НЕ является числом от 10 до 99'
            raise ValueError
    except BaseException:
        return error
    return ''


with open('registrations.txt', 'r', encoding='utf-8') as file:
    with open('registrations_bad.log', 'w', encoding='utf-8') as bad:
        with open('registrations_good.log', 'w', encoding='utf-8') as good:
            for line in file.readlines():
                if len(correct(line.split())) == 0:
                    good.write(f'{"".join(line)}')
                else:
                    bad.write(f'{"".join(line)} --- {correct(line)}')
