from random import randint


class House:
    fridge = 50
    cash = 0


class Human:
    satiety = 50
    dead = False

    def __init__(self, name, sweet_home):
        self.sweet_home = sweet_home
        self.name = name

    def brain(self):  # TODO предлагаю назвать act()
        dice = randint(1, 6)
        print(f'Бросок кубика для {self.name}: {dice}')
        if self.satiety < 20:
            self.feeding()
        elif self.sweet_home.fridge < 10:
            self.shopping()
        elif self.sweet_home.cash < 50:
            self.working()
        elif dice == 1:
            self.working()
        elif dice == 2:
            self.feeding()
        else:
            self.playing()

    def feeding(self):
        if self.sweet_home.fridge != 0:
            self.sweet_home.fridge -= 1
            print(f'{self.name} ест. Еды осталось: {self.sweet_home.fridge}\n')
        else:
            print('В холодильнике пусто!')
            # self.satiety -= 1
            self.shopping()

    def working(self):
        print(f'{self.name} работает\n')
        self.sweet_home.cash += 1
        self.satiety -= 1

    def playing(self):
        print(f'{self.name} играет на своем ПК\n')
        self.satiety -= 1

    def shopping(self):
        print(f'{self.name} идёт в магазин\n')
        if self.sweet_home.cash > 0:
            self.sweet_home.cash -= 1
            self.sweet_home.fridge += 1
        else:
            print('Не хватает средств на покупку еды\n')


if __name__ == '__main__':
    day = 1
    house = House()
    human_1 = Human('Алис', house)
    human_2 = Human('Юфи', house)
    while day < 366:
        if human_1.satiety >= 0:
            print(f'Сытость {human_1.name}: {human_1.satiety}')
            human_1.brain()
        else:
            print(f'{human_1.name} мертв(а)\n')
            human_1.dead = True
        if human_2.satiety >= 0:
            print(f'Сытость {human_2.name}: {human_2.satiety}')
            human_2.brain()
        else:
            print(f'{human_2.name} мертв(а)\n')
            human_2.dead = True

        print(f'Кол-во еды в холодильнике: {house.fridge}')
        print(f'Семейный бюджет в ящичке: {house.cash}\n')
        print(f'--- {day} день закончился ---\n')

        if human_1.dead and human_2.dead:
            print(f'{human_1.name} и {human_2.name} погибли!')
            break
        else:
            day += 1
