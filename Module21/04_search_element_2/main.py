def find_key(site_dict, key, deep_level=0):
    if key in site_dict:
        return site_dict[key]
    for i in site_dict.values():
        if isinstance(i, dict):
            result = find_key(site_dict[i], key, 0)  # TODO видимо просто i вместо site_dict[i]
            if result:
                break
    else:
        return None


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
# deep = input("Введите глубину")

print(find_key(site, key, 0))

#  Непонятен момент касательно "глубины"
# TODO добавьте 4й параметр в функцию для ограничения глубины поиска (числа рекурсивных вызов) и как функция превысит
#  его - она должна завершаться
