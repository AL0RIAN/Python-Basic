from random import randint


class KillError(Exception):
    """
    Класс, описывающий грех убийства. Родитель: Exception
    """
    pass


class DrunkError(Exception):
    """
    Класс, описывающий грех пьянства. Родитель: Exception
    """
    pass


class CarCrashError(Exception):
    """
    Класс, описывающий грех не трезвости за рулем? Родитель: Exception
    """
    pass


class GluttonyError(Exception):
    """
    Класс, описывающий грех объедения. Родитель: Exception
    """
    pass


class DepressionError(Exception):
    """
    Класс, описывающий грех уныния. Родитель: Exception
    """
    pass


class Human:
    """
    Класс, описывающий человека

    Attributes:
        karma (int): текущее кол-во кармы у человека
        sins (list): список грехов (исключений) человека
    """
    karma = 0
    sins = [KillError('Убийство - это ужасно!'), DrunkError('Не губи свою жизнь!'),
            CarCrashError('Я уже говорил о пьянстве?'), GluttonyError('Оставь место для святого духа!'),
            DepressionError('Не унывай. И не пей!')]

    def one_day(self):
        """
        Функция, определяющая случайным образом, согрешит ли человек или получит положительную карму

        Attributes:
            chance (int): случайное число от [1 до 10]

        :raise self.sins[randint(0, len(self.sins) - 1)]: если chance == 1
        """
        chance = randint(1, 10)
        if chance == 1:
            raise self.sins[randint(0, len(self.sins) - 1)]
        else:
            self.karma += randint(1, 7)
            print('Карма:', human.karma)


if __name__ == '__main__':
    human = Human()
    with open('karma.log', 'w', encoding='utf-8') as sin_log:
        while human.karma < 500:
            try:
                human.one_day()
            except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as sin:
                sin_log.write(f'{sin}\n')
