def correct(data):
    try:  # TODO в этой функции только выбрасываем исключения, а ловить исключения и обрабатывать их надо в главном
          #  цикле программы
        error = ''
        if len(data) != 3:
            error += 'IndexError: НЕ присутствуют все три поля: '
            # TODO поясняющие сообщения указывайте при выбрасывнаии исключения в круглых скобках
            raise IndexError('НЕ присутствуют все три поля:')  # TODO вот так, а класс исключения можно получить потом
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
        # TODO 1) используйте более конкретный класс исключения, тут (на самом деле ниже, в главном цикле программы)
        #  надо указать кортеж исключений которые
        #  выбрасываются. В любом случае, базовый класс всех простых исключений это Exception, а BaseException это
        #  "внутренности" реализации и обычно не используется
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
            # TODO обработка во всех исключений идентична, поэтому укажите кортеж классов, а сообщение
            #  записывайте в лог так: except (NameError, ...) as exc:
            #  error_message = f'{line.rstrip()} - {exc.__class__.__name__} - {exc}\n'
