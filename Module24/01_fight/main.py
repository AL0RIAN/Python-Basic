from random import randint


class Unit:
    health = 100

    def __init__(self, name='Воин'):
        self.name = name

    def get_damage(self):
        self.health -= 20
    # TODO добавьте метод "удар"/"атака"|"бой" принимающий через параметр объект врага и уменьшающий значение его
    #  атрибута health


unit_1 = Unit('Герберт')
unit_2 = Unit('Роберт')
while unit_1.health != 0 and unit_2.health != 0:
    initiative = randint(1, 2)
    print(f'Бросок 1к2: {initiative}')
    if initiative == 1:
        print(f'{unit_1.name} атакует по {unit_2.name} и наносит 20 единиц повреждений')
        unit_2.get_damage()
        print(f'У {unit_2.name} осталось {unit_2.health} очков здоровья\n')
    else:
        print(f'{unit_2.name} атакует по {unit_1.name} и наносит 20 единиц повреждений')
        unit_1.get_damage()
        print(f'У {unit_1.name} осталось {unit_1.health} очков здоровья\n')