country_count = int(input('Кол-во стран: '))
country_lst = []

for number in range(country_count):
    print('{} страна: '.format(number + 1), end='')
    country = input().split()
    country_lst.append(country)

country_dict = {country_lst[index][0]: country_lst[index][1:] for index in range(2)}

for index in range(3):
    print('\n{} город'.format(index + 1), end=': ')
    city = input()
    for country in country_dict:
        if city in country_dict.get(country):
            print('Город {0} расположен в стране {1}'.format(city, country))
            break
    else:
        print('По городу {} нет данных'.format(city))

