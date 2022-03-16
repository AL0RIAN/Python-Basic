from random import randint


class Unit:
    health = 100

    def __init__(self, name='Воин'):
        self.name = name

    def fight(self, other):
        print(f'{self.name} атакует по {other.name} и наносит 20 единиц повреждений')
        other.health -= 20
        print(f'У {other.name} осталось {other.health} очков здоровья\n')


if __name__ == '__main__':
    unit_1 = Unit('Герберт')
    unit_2 = Unit('Роберт')
    while unit_1.health != 0 and unit_2.health != 0:
        initiative = randint(1, 2)
        print(f'Бросок 1к2: {initiative}')
        if initiative == 1:
            unit_1.fight(unit_2)
        else:
            unit_2.fight(unit_1)
    if unit_1.health != 0:
        print(f'{unit_1.name} победил!')
    else:
        print(f'{unit_2.name} победил!')
