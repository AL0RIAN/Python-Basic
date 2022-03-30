import math


class Auto:
    """
    Родительский класс, описывающий автомобиль

    Args:
        x (int): координата по икс
        y (int): координата по игрек
        angle (int): угол
    """

    def __init__(self, x=0, y=0, angle=0):
        self.x = x
        self.y = y
        self.angle = angle

    def __str__(self):
        return f'X: {round(self.x, 2)}, Y: {round(self.y, 2)}, ANGLE: {self.angle}'

    def move(self, count):
        """
        Метод расчета конечных координат авто при движении

        :param count: расстояние
        :type: int
        """
        self.x += count * math.cos(self.angle)
        self.y += count * math.sin(self.angle)

    def turn(self, angle):
        """
        Метод изменения угла

        :param angle: угол
        :type: int
        """
        self.angle = angle


class Bus(Auto):
    """
    Дочерний класс, описывающий автобус. Родитель: Auto

    Attributes:
        passenger (int): кол-во пассажиров
        money (int): кол-во денег
    """
    passenger = 0
    money = 0

    def __str__(self):
        info = super().__str__()
        return f'{info}. MONEY: {self.money}, PASSENGER: {self.passenger}\n'

    def enter(self, count):
        """
        Метод прибавления входящих пассажиров к атрибуту passenger
        В случае достижения лимита выводится соответсвующее сообщение

        Args:
            count (int): кол-во входящих пассажиров
        """
        self.passenger += count
        if self.passenger > 30:
            self.passenger = 30
            print('Максимальное количество пассажиров!')

    def exit(self, count):
        """
        Метод убавления выходящих пассажиров из атрибута passenger

        Args:
            count (int): кол-во выходящих пассажиров
        """
        self.passenger -= count
        if self.passenger < 0:
            self.passenger = 0

    def move(self, count):
        """
        Метод расчета конечных координат автобуса при движении и выручки

        :param count: расстояние
        :type: int
        """
        super().move(count)
        self.money += self.passenger * count


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
            count_input = int(input('Сколько пассажиров заходят: '))
            bus.enter(count=count_input)
        elif choice == 2:
            count_input = int(input('Какое расстояние едем: '))
            bus.move(count=count_input)
        elif choice == 3:
            angle_new = int(input('Новый угол: '))
            bus.turn(angle_new)
        elif choice == 4:
            count_input = int(input('Сколько пассажиров выходит: '))
            bus.exit(count=count_input)
        elif choice == 5:
            break
        else:
            raise KeyError
        print(bus)
