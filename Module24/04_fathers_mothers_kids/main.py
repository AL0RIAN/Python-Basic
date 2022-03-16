from random import randint


class Parents:
    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def get_info(self):
        print(f'Имя: {self.name}\nВозраст: {self.age}')
        print('Дети: ', end='')
        for kid in self.children:
            print(kid.name, end=', ')
        print()

    def calm_down(self):
        for kid in self.children:
            if not kid.calm:
                kid.calm = True
                print(f'{self.name} успокаивает {kid.name}')
        print()

    def feeding(self):
        for kid in self.children:
            if kid.hunger:
                kid.hunger = False
                print(f'{self.name} кормит {kid.name}')
        print()


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
        print()

    def hunger_on(self):
        if self.hunger:
            self.hunger = False
        print()

    def bad_mood(self):
        if self.calm:
            self.calm = False
        print()


if __name__ == "__main__":
    children_list = []
    par_name = input('Введите имя родителя: ')
    par_age = int(input('Введите возраст родителя: '))
    count_of_child = int(input('Введите кол-во детей: '))
    for child in range(count_of_child):
        data = input(f'{child + 1} ребенок - введите имя и возраст: ').split()
        while True:
            if abs(int(data[1]) - par_age) < 16:
                print(
                    f'Ребенок младше родителя на {abs(int(data[1]) - par_age)}. Разница должна быть равна минимум 16!')
                data = input(f'{child + 1} ребенок - введите имя и возраст: ').split()
            else:
                children_list.append(Child(data))
                break
    parent_1 = Parents(par_name, par_age, children_list)
    print()
    while True:
        print('1 - информация о родителе\n'
              '2 - успокоить всех детей\n'
              '3 - покормить всех детей\n'
              '4 - ребенок плачет\n'
              '5 - ребенок голоден\n'
              '6 - информация о детях')
        choice = int(input('Выбор: '))
        print()
        if choice == 1:
            parent_1.get_info()
        if choice == 2:
            parent_1.calm_down()
        if choice == 3:
            parent_1.feeding()
        if choice == 4:
            child = parent_1.children[randint(0, len(parent_1.children) - 1)]
            child.bad_mood()
            print(f'{child.name} плачет!\n')
        if choice == 5:
            child = parent_1.children[randint(0, len(parent_1.children))]
            child.hunger_on()
            print(f'{child.name} проголодался!\n')
        if choice == 6:
            for child in parent_1.children:
                child.get_condition()
        if choice == 0:
            break
    print('Конец программы')
