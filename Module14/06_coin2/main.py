def coin_detector(x, y, r):
    if x <= r and y <= r:  # TODO надо вычислить расстояние от начала координат до этой точки и сравнить с радиусом.
                           #  Вернуть надо True или False, и на основе этого в основном коде вывести сообщение

        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))
coin_detector(x, y, r)
