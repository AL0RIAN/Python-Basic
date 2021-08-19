films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favorite = []

while True:
    film = input('Фильм: ')
    if film in films:
        favorite.append(film)
    else:
        print('Ошибка')
        break

print('Любимые фильмы:', favorite)
