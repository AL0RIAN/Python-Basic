n = int(input('Кол-во видеокарт: '))
videocards = []

for i in range(n):
    print(i + 1, 'Видеокарта:', end=' ')
    videocard = int(input())
    videocards.append(videocard)

maximum = videocards[0]
new_videcards = []

for i in videocards:
    if i > maximum:
        maximum = i

for i in videocards:
    if i != maximum:
        new_videcards.append(i)

print('\nСтарый список видеокарт:', videocards)
print('Новый список видеокарт:', new_videcards)
