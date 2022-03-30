class Property:
    """
    Базовый класс, описывающий имущество

    Args:
        worth(int): передаётся стоимость имущества
    """
    # TODO Считается хорошей практикой писать всегда на английском языке, кроме редких случаев когда об этом
    #  специально договаривается команда работающая над конкретным проектом
    def __init__(self, worth):
        self.worth = worth

    def __str__(self):
        return f'Налог: {self.tax()}'

    def tax(self):
        """
        Метод для расчета налога. Пуст; нужен для наследования.
        """
        pass


class Apartment(Property):
    """
    Класс, описывающий квартиру. Родитель: Property

    Args:
        worth(int): передаётся стоимость квартиры
    """

    def __init__(self, worth):
        super().__init__(worth)

    def __str__(self):
        info = super().__str__()
        return f'\nКвартира. {info}'

    def tax(self):
        """
        Метод для расчёта налога

        :return: self.worth * 0.001
        :rtype: float
        """
        return self.worth * 0.001


class Car(Property):
    """
    Класс, описывающий машину. Родитель: Property

    Args:
        worth(int): передаётся стоимость машины
    """

    def __init__(self, worth):
        super().__init__(worth)

    def __str__(self):
        info = super().__str__()
        return f'\nМашина. {info}'

    def tax(self):
        """
        Метод для расчёта налога

        :return: 0.005 * self.worth
        :rtype: float
        """
        return 0.005 * self.worth


class CountryHouse(Property):
    """
    Класс, описывающий загородный дом. Родитель: Property

     Args:
        worth(int): передаётся стоимость дома
    """

    def __init__(self, worth):
        super().__init__(worth)

    def __str__(self):
        info = super().__str__()
        return f'\nДом. {info}'

    def tax(self):
        """
        Метод для расчёта налога

        :return: 0.002 * self.worth
        :rtype: float
        """
        return 0.002 * self.worth


if __name__ == '__main__':
    money = int(input('Кол-во денег: '))
    money_apart = int(input('Стоимость квартиры: '))
    apart = Apartment(money_apart)
    money_car = int(input('Стоимость машины: '))
    car = Car(money_car)
    money_house = int(input('Стоимость дома: '))
    house = CountryHouse(money_house)

    print(apart)
    print(car)
    print(house)

    sum_tax = apart.tax() + car.tax() + house.tax()
    if money - sum_tax < 0:
        print('Нужно денег:', abs(money - sum_tax))
