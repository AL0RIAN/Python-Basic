phone_book = {}

while True:
    print("Текущий список", phone_book)

    print("\n1 - добавить, 2 - найти человека")
    action = int(input("Введите действие: "))
    if action == 1:
        name = tuple(input("Введите имя и фамилию: ").split())
        if name in phone_book.keys():
            print("Такой контакт уже существует!")
        else:
            number = int(input("Введите номер телефона: "))
            phone_book[name] = number
            print("Контакт добавлен!")
            print("-" * 30, '\n')
    elif action == 2:
        name = input("Введите фамилию искомого контакта: ")
        print("Контакты с такой фамилией:")
        results = 0
        for key in phone_book.keys():
            if key[1] == name:
                print("    {0} {1} - {2}".format(key[0], key[1], phone_book[key]))
                results += 1
        if results == 0:
            print("    По данной фамилии ничего не найдено\n")
        print("-" * 30, '\n')
