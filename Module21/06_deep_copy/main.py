def deepcopy(inList):
    if isinstance(inList, list):
        return list( map(deepcopy, inList) )
    return inList

# def deepcopy(struct, copy, deep=0):
#     for value in struct:
#         if isinstance(struct[value], dict):
#             copy[value] = deepcopy(struct[value], copy)
#             return struct[value]
#         else:
#             return struct[value]


def rebranding(struct, brand_name):
    if 'title' in struct:
        struct['title'] = 'Куплю/продам {} недорого'.format(brand_name)
        return True
    elif 'h2' in struct:
        struct['h2'] = 'У нас самая низкая цена на {}'.format(brand_name)
        return True
    for value in struct.values():
        if isinstance(value, dict):
            if rebranding(value, brand_name):
                break
    return struct


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

# count = int(input("Введите кол-во брендов: "))
count = 1
brands = {}
# for counter in range(count):
# brand = input("Введите название продукта для нового сайта: "

# deepcopy(site, {})
# print(deepcopy(site, {}))
brands['samsung'] = rebranding(deepcopy(site, {}), 'samsung')
print(brands['samsung'])
print(site)
# НАМ НУЖНО СДЕЛАТЬ "ГЛУБОКУЮ КОПИЮ" С ПОМОЩЬЮ РЕКУРСИИ.
