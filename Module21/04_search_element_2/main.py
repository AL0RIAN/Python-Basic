def find_key(site_dict, key_name, deep_level=997, count=0):
    if key_name in site_dict or count == deep_level:
        return site_dict[key_name]
    count += 1
    for value in site_dict.values():
        if isinstance(value, dict):
            if find_key(value, key_name):
                return find_key(value, key_name, deep_level, count)


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key = input("Введите ключ: ")
answer = input("Ввести глубину поиска - y/n: ").lower()

if answer == 'y':
    deep = int(input("Введите глубину: "))
    print(find_key(site, key, deep))
elif answer == 'n':
    print(find_key(site, key))
