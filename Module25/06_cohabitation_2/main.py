from random import randint


class House:
    """
    Класс, описывающий дом

    Attribute:
        money (int): текущий бюджет в доме
        fridge (int): кол-во еды в доме
        whiskas (int): кол-во еды для котика в доме
        dirty (int): уровень загрязнения дома
    """
    money = 100
    fridge = 50
    whiskas = 30
    dirty = 0

    def __str__(self):
        return f'\nСитуация в доме\n' \
               f'Деньги: {self.money}\n' \
               f'Еда: {self.fridge}\n' \
               f'Вискас: {self.whiskas}\n' \
               f'Уровень грязи: {self.dirty}\n'


class Creature:
    """
    Базовый класс, описывающий живое существо

    Attributes:
        satiety (int): текущая сытость существа
        dead (bool): статус живо/мертво существо

    Args:
        name (str): имя существа
        sweet_home (__main__.House): дом, в котором живет существо
    """
    satiety = 30
    dead = False

    def __init__(self, name, sweet_home):
        self.name = name
        self.sweet_home = sweet_home

    def __str__(self):
        return f'Имя: {self.name}\nСытость: {self.satiety}'

    def feeding(self, count):
        """
        Метод, реализующий питание существа.
        Если в холодильнике дома достаточно еды, то
        сытость существа увеличивается на count, а кол-во еды
        в холодильнике уменьшается на count. Иначе сообщение о том,
        что в холодильнике недостаточно еды и минус 10 единиц сытости
        существу.

        :param count: кол-во потребляемой пищи
        :type: int
        """
        if self.sweet_home.fridge >= count:
            self.satiety += count
            self.sweet_home.fridge -= count
            if self.sweet_home.fridge <= 0:
                print(f'{self.name} съел всю еду!')
                self.sweet_home.fridge = 0
        else:
            self.satiety -= 10
            print(f'{self.name} идет кушать, а холодильник-то пуст!')

    def still_alive_is(self):
        """
        Метод, проверяющий статус существа
        """
        if self.satiety <= 0:
            self.dead = True


class Husband(Creature):
    """
    Дочерний класс, описывающий мужа. Родитель: Creature

    Attributes:
        happiness (int): текущее кол-во счастья мужа

    Args:
        name (str): имя существа
        sweet_home (__main__.House): дом, в котором живет существо
    """
    happiness = 100

    def __init__(self, name, sweet_home):
        super().__init__(name, sweet_home)

    def __str__(self):
        info = super().__str__()
        return f'{info}\nСчастье: {self.happiness}\n'

    def act(self, cat_status):
        """
        Метод, координирующий действия существа.
        В зависимости от случайно выбранного числа [1 до 6]
        и текущей ситуации в доме будет выбрано действие.

        :param cat_status: статус жив/мертв (кот)
        :type: bool
        """
        dice = randint(1, 6)
        if dice == 6 and not cat_status:
            self.pat_cat()
        if self.satiety < 15:
            self.feeding(randint(10, 30))
        elif self.sweet_home.money < 50:
            self.working()
        elif dice == 1:
            self.working()
        elif dice == 2:
            self.feeding(15)
        else:
            self.playing()

    def playing(self):
        """
        Муж играет и повышает счастье, понижает сытость
        """
        print(f'{self.name} играет в Elden Ring.')
        self.satiety -= 10
        self.happiness += 20

    def working(self):
        """
        Муж работает и получает деньги, понижает сытость
        """
        print(f'{self.name} работает в IT компании.')
        self.satiety -= 10
        self.sweet_home.money += 150

    def pat_cat(self):
        """
        Муж гладит кота и получает счастье
        """
        print(f'{self.name} удостоился шанса погладить котика, проходя по своим делам!!!')
        self.happiness += 5

    def still_alive_is(self):
        "Проверка статуса жив/мертв"
        super().still_alive_is()
        if self.happiness < 10:
            self.dead = True


class Wife(Creature):
    """
    Дочерний класс, описывающий жену. Родитель: Creature

    Attributes:
        happiness (int): текущее кол-во счастья жены

    Args:
        name (str): имя существа
        sweet_home (__main__.House): дом, в котором живет существо
    """
    happiness = 100

    def __init__(self, name, sweet_home):
        super().__init__(name, sweet_home)

    def __str__(self):
        info = super().__str__()
        return f'{info}\nСчастье: {self.happiness}\n'

    def act(self, cat_status):
        """
        Метод, координирующий действия существа.
        В зависимости от случайно выбранного числа [1 до 7]
        и текущей ситуации в доме будет выбрано действие.

        :param cat_status: статус жив/мертв (кот)
        :type: bool
        """
        dice = randint(1, 7)
        if dice == 7 and not cat_status:
            self.pat_cat()
        if self.sweet_home.fridge < 30:
            self.buy_food()
        elif self.satiety < 20:
            self.feeding(randint(10, 30))
        elif self.sweet_home.whiskas < 15:
            self.buy_whiskas()
        elif self.sweet_home.dirty > 10:
            self.cleaning()
        elif dice == 1:
            self.feeding(15)
        elif dice == 2:
            self.shooping()
        else:
            self.buy_food()

    def buy_food(self):
        """
        Жена покупает продукты: повышает кол-во еды на 30, понижая деньги на 30 и сытость на 10
        """
        print(f'{self.name} покупает 30 единиц еды.')
        self.sweet_home.fridge += 30
        self.sweet_home.money -= 30
        self.satiety -= 10

    def buy_whiskas(self):
        """
        Жена покупает еду для кота: повышает кол-во еды на 10% от денег в доме,
        понижая деньги на столько же и сытость на 10
        """
        print(f'{self.name} покупает {round(0.1 * self.sweet_home.money)} единиц Вискаса.')
        self.sweet_home.whiskas += round(0.1 * self.sweet_home.money)
        self.satiety -= 10

    def cleaning(self):
        """
        Жена убирается, понижая уровень грязи в доме и понижая сытость на 10
        """
        result = randint(1, self.sweet_home.dirty)
        self.sweet_home.dirty -= result
        self.satiety -= 10
        print(f'{self.name} убирается в доме и уничтожает {result} единиц грязи')

    def shooping(self):
        """
        Жена покупает шубу сильно повышая счастье и понижая сытость
        """

        print(f'{self.name} очень хочет купить шубу.', end=' ')

        if self.sweet_home.money >= 350:
            self.sweet_home.money -= 350
            self.happiness += 60
            print('И очень её покупает!')
        else:
            print('Но средств не хватает. Идёт выносить мозг мужу.')
            self.happiness -= 5
        self.satiety -= 10

    def pat_cat(self):
        """
        Жена гладит кота и получает счастье
        """
        print(f'{self.name} удостоилась шанса погладить котика, проходя по своим делам!!!')
        self.happiness += 5

    def still_alive_is(self):
        """
        Проверка статуса жива/мертва
        """
        super().still_alive_is()
        if self.happiness < 10:
            self.dead = True


class Cat(Creature):
    """
    Дочерний класс, описывающий кота. Родитель: Creature

    Args:
        name (str): имя существа
        sweet_home (__main__.House): дом, в котором живет существо
    """
    def __init__(self, name, sweet_home):
        super().__init__(name, sweet_home)

    def act(self):
        """
        Метод, координирующий действия существа.
        В зависимости от случайно выбранного числа [1 до 3]
        и текущей ситуации в доме будет выбрано действие.
        """
        dice = randint(1, 3)
        if self.satiety < 15:
            self.feeding(randint(1, 10))
        elif dice == 1:
            self.vandalism()
        else:
            self.sleeping()

    def sleeping(self):
        """
        Кот спит и тратит сытость
        """
        print(f'{self.name} спит')
        self.satiety -= 10

    def vandalism(self):
        """
        Кот дерёт обои, повышая уровень грязи в доме
        """
        print(f'{self.name} портит обои!')
        self.sweet_home.dirty += 5

    def feeding(self, count):
        """
        Кот кушает, повышая сытость на count, понижая кол-во Вискаса в доме
        :param count: кол-во потребляемого Вискаса
        :type: int
        """
        print(f'{self.name} кушает.')
        self.sweet_home.whiskas -= count
        self.satiety += count * 2


if __name__ == '__main__':
    house = House()
    human_1 = Husband('Джон', house)
    human_2 = Wife('Лора', house)
    cat = Cat('Бобби Котик', house)
    day = 1

    while (not human_1.dead) and (not human_2.dead) and (day < 366):
        print(f'\nДень #{day}')
        human_2.act(cat.still_alive_is())
        human_1.act(cat.still_alive_is())
        cat.act()
        human_1.still_alive_is()
        human_2.still_alive_is()

        if house.dirty > 90:
            human_1.happiness -= 10
            human_2.happiness -= 10

        print(house)
        print(human_1)
        print(human_2)
        print(cat)

        day += 1
