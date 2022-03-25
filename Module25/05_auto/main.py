class Auto:
    def __init__(self, x=0, y=0, angle=0):
        self.x = x
        self.y = y
        self.angle = angle

    def __str__(self):
        return f'X: {self.x}, Y: {self.y}, ANGLE: {self.angle}'

    def move(self):
        # TODO метод должен принимать один параметр - расстояние - и пересчитывать координаты в соответствии
        #  с передвижением из текущей точки (self.x, self.y) по направлению self.angle
        count = int(input('Какое расстояние едем: '))  # TODO вместо работы с консолью используйте параметр метода,
                                                       #  а запрос перемещения у пользователя программы делайте в
                                                       #  основом коде программы
        if 0 < self.angle < 90:  # TODO угол может быть любым, расчёт надо делать по тригонометрическим формулам без
                                 #  использования условного оператора
            self.x += count
            self.y += count
        elif 90 < self.angle < 180:
            self.x -= count
            self.y += count
        elif 180 < self.angle < 270:
            self.x -= count
            self.y -= count
        elif 270 < self.angle < 360:
            self.x += count
            self.y -= count
        elif self.angle == 0 or self.angle == 360:
            self.x += count
        elif self.angle == 90:
            self.y += count
        elif self.angle == 180:
            self.x -= count
        elif self.angle == 270:
            self.y -= count
        return count

    def turn(self, angle):
        self.angle = angle
        print()  # TODO в коде класса не используйте работу с консолью


class Bus(Auto):
    passenger = 0
    money = 0

    def __init__(self, x, y, angle):  # TODO переопределяем методы только для изменения их логики, а тут этого нет
        super().__init__(x, y, angle)

    def __str__(self):
        info = super().__str__()
        return f'{info}. MONEY: {self.money}, PASSENGER: {self.passenger}\n'

    def enter(self):
        count = int(input('Сколько пассажиров садится: '))
        self.passenger += count
        if self.passenger > 30:
            self.passenger = 30
            print('Максимальное количество пассажиров!')
        print()

    def exit(self):
        count = int(input('Сколько пассажиров выходит: '))
        self.passenger -= count
        if self.passenger < 0:
            self.passenger = 0
        print()

    def move(self):
        self.money += self.passenger * super().move()
        print()


if __name__ == '__main__':
    x_start = int(input('X: '))
    y_start = int(input('Y: '))
    angle_start = int(input('Angle: '))
    bus = Bus(x=x_start, y=y_start, angle=angle_start)
    print()
    while True:
        print(
            '1 - пассажиры входят\n'
            '2 - автобус едет\n'
            '3 - автобус поворачивает\n'
            '4 - пассажиры выходят\n'
            '5 - конец программы')
        choice = int(input('Выбор: '))
        print()

        if choice == 1:
            bus.enter()
        elif choice == 2:
            bus.move()
        elif choice == 3:
            angle_new = int(input('Угол поворота: '))
            bus.turn(angle_new)
        elif choice == 4:
            bus.exit()
        elif choice == 5:
            break
        else:
            raise KeyError
        print(bus)
