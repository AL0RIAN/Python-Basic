from random import randint


class Parents:
    def __init__(self, name, age, count):
        self.name = name
        self.age = age
        self.children = [Child(input(f'{child + 1} ребенок - введите имя и возраст: ').split()) for child in
                         range(count)]  # TODO 1) список объектов детей формируйте в основном коде
                                        #  программы, это даёт гораздо больше возможностей по использованию класса
                                        #  2) до присваивания списка детей атрибуту, надо проверить ограничение по
                                        #  возрасту указанное в задании

    def get_info(self):
        print(f'Имя: {self.name}\nВозраст: {self.age}')
        print('Дети: ', end='')
        for child in self.children:
            print(child.name, end=', ')
        print('\n')

    def calm_down(self):
        for child in self.children:
            if not child.calm:
                child.calm = True
                print(f'{self.name} успокаивает {child.name}')
        print('\n')

    def feeding(self):
        for child in self.children:
            if child.hunger:
                child.hunger = False
                print(f'{self.name} кормит {child.name}')
        print('\n')


class Child:
    hunger = False
    calm = True

    def __init__(self, info):
        self.name = info[0]
        self.age = info[1]

    def get_condition(self):
        print(f'Имя: {self.name}\nВозраст: {self.age}')
        if self.hunger:
            print(f'{self.name} голоден!')
        else:
            print(f'{self.name} cыт(а)')
        if not self.calm:
            print(f'{self.name} плачет!')
        else:
            print(f'{self.name} спокоен/спокойна')
        print('\n')

    def hunger_on(self):
        if self.hunger:
            self.hunger = False
        print('\n')

    def bad_mood(self):
        if self.calm:
            self.calm = False
        print('\n')


if __name__ == "__main__":
    par_name = input('Введите имя родителя: ')
    par_age = int(input('Введите возраст родителя: '))
    count_of_child = int(input('Введите кол-во детей: '))
    parent_1 = Parents(par_name, par_age, count_of_child)
    print('\n')
    while True:
        print('1 - информация о родителе\n'
              '2 - успокоить всех детей\n'
              '3 - покормить всех детей\n'
              '4 - ребенок плачет\n'
              '5 - ребенок голоден\n'
              '6 - информация о детях')
        choice = int(input('Выбор: '))
        print('\n')
        if choice == 1:
            parent_1.get_info()
        if choice == 2:
            parent_1.calm_down()
        if choice == 3:
            parent_1.feeding()
        if choice == 4:
            child = parent_1.children[randint(0, len(parent_1.children))]
            child.bad_mood()
            print(f'{child.name} плачет!\n')
        if choice == 5:
            child = parent_1.children[randint(0, len(parent_1.children))]
            child.hunger_on()
            print(f'{child.name} проголодался!\n')
        if choice == 6:
            for child in parent_1.children:
                child.get_condition()
            else:
                print(f'У {parent_1.name} нет детей!')
        if choice == 0:
            break
    print('Конец программы')
