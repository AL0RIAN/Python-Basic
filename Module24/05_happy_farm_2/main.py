class Potato:
    states = {0: 'отсутствует', 1: 'росток', 2: 'зеленое', 3: 'зрелое'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def is_ripe(self):
        if self.state == 3:
            return True
        return False

    def grow(self):
        if self.state < 3:
            self.state += 1

    def print_state(self):
        print('Картошка {} сейчас {}'.format(self.index, Potato.states[self.state]))


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potato in self.potatoes:
            i_potato.grow()

    def are_all_ripe(self):
        for i_potato in self.potatoes:
            if not i_potato.is_ripe():
                return False
        else:
            return True


class Gardener:
    def __init__(self, name):
        self.name = name

    def care(self, garden):
        garden.grow_all()

    def harvest(self, garden):
        if garden.are_all_ripe():
            garden.potatoes = []
            print('Вся картошка созрела')
            print(f'{self.name} собрал урожай! Грядка пустая')
        else:
            print('Картошка ещё не созрела')


if __name__ == "__main__":
    garden_1 = PotatoGarden(5)
    name_gar = input('Имя садовника: ')
    gardener = Gardener(name_gar)

    while True:
        if not garden_1.are_all_ripe():
            gardener.care(garden_1)
        else:
            gardener.harvest(garden_1)
            break
