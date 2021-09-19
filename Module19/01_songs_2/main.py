violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

count = int(input('Сколько песен выбрать? '))
time = []

for index in range(count):
    print('Название {} песни'.format(index + 1), end=': ')
    name = input()
    time.append(violator_songs[name])

print('\nОбщее время звучания песен: {} минут'.format(round(sum(time), 2)))



