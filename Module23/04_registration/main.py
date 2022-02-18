def correct(data):
    if len(data) != 3:
        raise IndexError('IndexError: НЕ присутствуют все три поля: ')
    elif not data[0].isalpha():
        raise NameError('NameError: Поле имени содержит НЕ только буквы')
    elif not ('@' in data[1] and '.' in data[1]):
        raise SyntaxError('SyntaxError: Поле емейл НЕ содержит @ и .(точку)')
    elif not (10 <= int(data[2]) < 99):
        raise ValueError('ValueError: Поле возраст НЕ является числом от 10 до 99')


with open('registrations.txt', 'r', encoding='utf-8') as file:
    with open('registrations_bad.log', 'w', encoding='utf-8') as bad:
        with open('registrations_good.log', 'w', encoding='utf-8') as good:
            for line in file.readlines():
                try:
                    correct(line.split())
                    good.write(f'{"".join(line)}')
                except (IndexError, NameError, SyntaxError, ValueError) as error:
                    bad.write(f'{line.rstrip()} - {error.__class__.__name__} - {error}\n')
