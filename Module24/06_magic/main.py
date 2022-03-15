from random import randint


class Water:
    description = 'Это стихия Воды'
    name = 'Вода'

    def __add__(self, other):
        if type(other) == Air:
            return Storm()
        elif type(other) == Fire:
            return Steam()
        elif type(other) == Earth:
            return Dirt()
        else:
            return Abyss().chaos_of_abyss[randint(0, len(Abyss().chaos_of_abyss) - 1)]


class Air:
    description = 'Это стихия Воздуха'
    name = 'Воздух'

    def __add__(self, other):
        if type(other) == Water:
            return Storm()
        elif type(other) == Fire:
            return Lightning()
        else:
            return Abyss().chaos_of_abyss[randint(0, len(Abyss().chaos_of_abyss) - 1)]


class Fire:
    description = 'Это стихия Огня'
    name = 'Огонь'

    def __add__(self, other):
        if type(other) == Water:
            return Steam()
        elif type(other) == Air:
            return Lightning()
        elif type(other) == Earth:
            return Lava()
        else:
            return Abyss().chaos_of_abyss[randint(0, len(Abyss().chaos_of_abyss) - 1)]


class Earth:
    description = 'Это стихия Земли'
    name = 'Земля'

    def __add__(self, other):
        if type(other) == Water:
            return Dirt()
        elif type(other) == Air:
            return Dust()
        elif type(other) == Fire:
            return Lava()
        else:
            return Abyss().chaos_of_abyss[randint(0, len(Abyss().chaos_of_abyss) - 1)]


class Storm:
    description = 'Это стихия Шторма'
    name = 'Шторм'


class Steam:
    description = 'Это стихия Пара'
    name = 'Пар'


class Dirt:
    description = 'Это стихия Грязи'
    name = 'Грязь'


class Lightning:
    description = 'Это стихия Молнии'
    name = 'Молния'


class Dust:
    description = 'Это стихия Пыли'
    name = 'Пыль'


class Lava:
    description = 'Это стихия Лавы'
    name = 'Лава'


class Abyss:
    description = 'Это стихия Бездны. Контакт с ней несет случайный результат!'
    name = 'Бездна'
    chaos_of_abyss = [Water(), Air(), Fire(), Earth(), Storm(), Steam(), Dirt(), Lightning(), Dust(), Lava()]

    def __add__(self, other):
        return self.chaos_of_abyss[randint(0, len(self.chaos_of_abyss) - 1)]


class Elementals:
    def __init__(self, name):
        self.name = name

    def distribution(self):
        if self.name == 'вода' or self.name == 'water':
            return Water()
        elif self.name == 'воздух' or self.name == 'air':
            return Air()
        elif self.name == 'огонь' or self.name == 'fire':
            return Fire()
        elif self.name == 'земля' or self.name == 'earth':
            return Earth()
        else:
            return Abyss()


if __name__ == "__main__":
    while True:
        print('-Впишите стихии, которые вы хотите соединить-\n-Чтобы взвать к Бездне, введите что угодно!-\n')
        first_elem = input('Первый элемент: ').lower()
        second_elem = input('Второй элемент: ').lower()

        first_elem = Elementals(first_elem).distribution()
        second_elem = Elementals(second_elem).distribution()

        if first_elem + second_elem:
            result = first_elem + second_elem
            print(f'{first_elem.name} + {second_elem.name} = {result.name}\n')

        else:
            print(f'{first_elem.name} + {second_elem.name} = стихии испарились без эффекта!\n')
