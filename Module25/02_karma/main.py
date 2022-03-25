from random import randint


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class Human:
    karma = 0
    sins = [KillError('Убийство - это ужасно!'), DrunkError('Не губи свою жизнь!'),
            CarCrashError('Я уже говорил о пьянстве?'), GluttonyError('Оставь место для святого духа!'),
            DepressionError('Не унывай. И не пей!')]

    def one_day(self):
        chance = randint(1, 10)
        if chance == 1:
            raise self.sins[randint(0, len(self.sins) - 1)]
        else:
            self.karma += randint(1, 7)
            print('Карма:', human.karma)


if __name__ == '__main__':
    human = Human()
    while human.karma < 500:
        # TODO возьмите вызов метода one_day "под защиту" конструкции try..except, логгируйте исключения аналогично
        #  решению задачи 4 в модуле 23
        human.one_day()
