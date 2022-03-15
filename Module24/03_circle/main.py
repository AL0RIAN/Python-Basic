import math


class Circle:
    def __init__(self, x=0, y=0, r=1):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r

    def increase(self, k):
        self.r *= k

    def is_cross(self, other):
        if self.x == other.x:
            if self.r + other.r > abs(self.y - other.y):
                print('Окружности пересекаются\n')
            else:
                print('Окружности не пересекаются\n')
        elif self.y == other.y:
            if self.r + other.r > abs(self.x - other.x):
                print('Окружности пересекаются\n')
            else:
                print('Окружности не пересекаются\n')
        else:
            if (self.r + other.r) ** 2 > abs((self.x - other.x) ** 2 - (self.y - other.y) ** 2):
                print('Окружности пересекаются\n')
            else:
                print('Окружности не пересекаются\n')


if __name__ == "__main__":
    circles = []
    count = int(input('Количество окружностей: '))
    for _ in range(count):
        choice = int(input('Изменить значения по умолчанию? 1/0: '))
        if choice:
            x_cir = int(input('Введите x: '))
            y_cir = int(input('Введите y: '))
            radius = int(input('Введите radius: '))
            circles.append(Circle(x_cir, y_cir, radius))
        else:
            circles.append(Circle())
    print()
    for circle in range(len(circles)):
        print(
            f'{circle} окружность: '
            f'x = {circles[circle].x}; y = {circles[circle].y}; radius = {circles[circle].r}')
    while True:
        number = int(input('Выберите окружность начиная с нуля (несуществующий номер - выход): '))
        print()
        if number in range(0, len(circles)):
            print('1 - найти площадь\n'
                  '2 - найди периметр\n'
                  '3 - увечить окружность в K раз\n'
                  '4 - определить, пересекается ли данные окружности')
            choice = int(input('Выбор: '))
            print()
            if choice == 1:
                print(f'Площадь: {circles[number].area()}')
            elif choice == 2:
                print(f'Периметр: {circles[number].perimeter()}')
            elif choice == 3:
                k = int(input('Введите K: '))
                circles[number].increase(k)
                print(f'x = {circles[number].x}; y = {circles[number].y}; radius = {circles[number].r}')
            elif choice == 4:
                second = int(input('Введите номер второй окружности: '))
                circles[number].is_cross(circles[second - 1])
        else:
            print('Конец программы')
            break
