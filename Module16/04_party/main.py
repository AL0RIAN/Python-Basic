def count_of_guests(list_of_guests):
    if len(list_of_guests) < 6:  # TODO аналогично предыдущему
        return True
    else:
        return False


guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
condition = ''

while True:
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    condition = input('Гость пришел или ушел? ')
    if condition == 'пришел':
        guest = input('Имя гостя: ')
        if count_of_guests(guests):
            print('Привет,', guest)
            guests.append(guest)
        else:
            print('Прости,', guest, 'но мест нет')
    elif condition == 'ушел':
        guest = input('Имя гостя: ')
        print('Пока,', guest, '!')
        guests.remove(guest)
    elif condition == 'Пора спать':
        break
    else:
        print('Неверный ввод!')

print('\nВечеринка закончилась, все легли спать.')
