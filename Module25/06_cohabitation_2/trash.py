from random import randint


class House:
    money = 100
    fridge = 50
    whiskas = 30
    dirt = 0


class Human:
    satiety = 30
    happiness = 100
    dead = False

    def __init__(self, name, sweet_home):
        self.name = name
        self.sweet_home = sweet_home

    def __str__(self):
        return f'\n{self.name}\nСытость: {self.satiety}\nСчастье: {self.happiness}\n'

    def feeding(self, food):
        if self.sweet_home.fridge <= 0:
            print('Холодильник пуст!')
            self.sweet_home.fridge = 0
            self.satiety -= 1
            return 0
        else:
            self.satiety += food
            self.sweet_home.fridge -= food
            return 1


class Husband(Human):
    def __init__(self, name, sweet_home):
        super().__init__(name, sweet_home)

    def act(self):
        dice = randint(1, 5)

        if self.satiety < 20:
            self.feeding(randint(1, 30))
        elif self.sweet_home.money < 50:
            self.working()
        elif dice == 1:
            self.working()
        elif dice == 2:
            self.feeding(randint(1, 30))
        else:
            self.playing()

    def playing(self):
        self.satiety -= 10
        self.happiness += 20

    def working(self):
        self.satiety -= 10
        self.sweet_home.money += 150


# Генерируется число кубика от 1 до 6
# Если сытость < 20, то поесть
# Иначе если еды в доме < 10, то сходить в магазин
# Иначе если денег в доме < 50, то работать
# Иначе если кубик равен 1, то работать
# Иначе если кубик равен 2, то поесть

class Wife(Human):
    def __init__(self, name, sweet_home):
        super().__init__(name, sweet_home)

    def act(self):
        dice = randint(1, 6)

        if self.satiety < 20:
            if not self.feeding(randint(1, 30)):
                self.buy_food(30, 0)


    def buy_food(self, food, whiskas):
        self.satiety -= 10
        self.sweet_home.money -= food
        self.sweet_home.fridge += food
        self.sweet_home.money -= food
        self.sweet_home.whiskas += whiskas

    def shooping(self):
        self.satiety -= 10
        self.sweet_home.money -= 350
        self.happiness += 60

    def cleaning(self, count):
        self.satiety -= 10
        self.sweet_home.dirt -= count


class Cat:
    satiety = 30

    def __init__(self, name, sweet_home):
        self.name = name
        self.sweet_home = sweet_home

    def feeding(self, food):
        if food > 10 or food <= 0:
            while (food > 10) or (food <= 0):
                food = int(input('Введите значение от 1 до 10: '))
        else:
            self.satiety -= food

    def sleeping(self):
        self.satiety -= 10

    def vandalism(self):
        self.satiety -= 10
        self.sweet_home.dirt += 5


if __name__ == '__main__':
    house = House()
    husband = Husband('George', house)
    wife = Wife('Eleonor', house)
    day = 1

    while day != 366:
        print(f'-День {day}-')
        husband.act()
        print(husband)
        print(f'-Конец {day} дня-\n')
        day += 1
