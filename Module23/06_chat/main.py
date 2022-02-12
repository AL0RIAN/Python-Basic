import datetime

user_name = input("Введите имя пользователя: ")
user_cache = [user_name]

try:
    while True:
        print()
        print(
            "Посмотреть текущий текст чата - 1\nОтправить сообщение - 2\nСменить пользователя - 3\nВыход - 4\n")
        choice = int(input("Действие: "))
        print()
        if choice == 1:
            print('-' * 30)
            if user_name == user_cache[0]:
                with open('history1.txt', 'r', encoding='utf-8') as user1:
                    for line in user1.readlines():
                        print(line)
            else:
                with open('history2.txt', 'r', encoding='utf-8') as user2:
                    for line in user2.readlines():
                        print(line)
            print('-' * 30)
        if choice == 2:
            message = input('Ввод: ')
            date_now = datetime.datetime.now().strftime('%H:%M:%S')
            with open('history1.txt', 'a', encoding='utf-8') as user1:
                with open('history2.txt', 'a', encoding='utf-8') as user2:
                    if user_name == user_cache[0]:
                        user1.write(f'({date_now}) Вы: {message}\n')
                        user2.write(f'({date_now}) {user_name}: {message}\n')
                    else:
                        user2.write(f'({date_now}) Вы: {message}\n')
                        user1.write(f'({date_now}) {user_name}: {message}\n')
        if choice == 3:
            user_name = input("Смена пользователя: ")
            if user_name not in user_cache and len(user_cache) != 2:
                user_cache.append(user_name)
            else:
                while len(user_cache) == 2 and user_name not in user_cache:
                    print(f'{user_name} не является участником чата. Попробуйте ещё раз:')
                    user_name = input()
        if choice == 4:
            print("Чат завершен. История очищена")
            break
finally:
    with open('history1.txt', 'w', encoding='utf-8') as user1:
        pass
    with open('history2.txt', 'w', encoding='utf-8') as user2:
        pass

