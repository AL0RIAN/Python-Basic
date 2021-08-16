def coin_detector(x, y, r):
    if x <= r and y <= r:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


x = float(input('X: '))
y = float(input('Y: '))
r = float(input('Введите радиус: '))
coin_detector(x, y, r)
