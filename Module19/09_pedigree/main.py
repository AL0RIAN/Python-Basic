n = int(input('Введите количество человек: '))
height = {}
family = {}

for index in range(n - 1):
    print(index + 1, 'пара: ', end='')
    para = input().split()
    height[para[0]] = para[1]
    family[para[0]] = 0
    family[para[1]] = 0

for i in height:
    s = i
    while s in height:
        s = height[s]
        family[i] += 1
print()

print('“Высота” каждого члена семьи:')
for i in sorted(family):
    print(i, family[i])