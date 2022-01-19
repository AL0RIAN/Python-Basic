import copy


def rebranding(struct, brand_name):
    if 'title' in struct:
        struct['title'] = 'Куплю/продам {} недорого'.format(brand_name)
        return 1
    if 'h2' in struct:
        struct['h2'] = 'У нас самая низкая цена на {}'.format(brand_name)
        return 1
    for value in struct:
        rebranding(struct[value], brand_name)
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

count = int(input('Введите кол-во сайтов: '))
brands = {}
for brand in range(count):
    new = copy.deepcopy(site)
    name = input("Введите название нового продукта: ")
    brands[name] = (rebranding(new, name))
    for key in brands.keys():
        print('Сайт для {}:\nsite = {}'.format(key, brands[key]))
    print()
