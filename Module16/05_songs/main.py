violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

n = int(input('Сколько песен выбрать? '))
minutes = 0

for i in range(n):
    print('Название', i + 1, 'песни:', end=' ')
    name = input()
    for song in violator_songs:  # TODO Аналогично предыдущему (распаковка списка)
        if song[0] == name:
            minutes += song[1]

print('\nОбщее время звучания песен:', round(minutes, 2), 'минут')