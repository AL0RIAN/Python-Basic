class Property:
    def __init__(self, worth):
        self.worth = worth

    def __str__(self):
        return f'Налог: {self.tax()}'

    def tax(self):
        pass


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def __str__(self):
        info = super().__str__()
        return f'\nКвартира. {info}'

    def tax(self):
        return self.worth * 0.001


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def __str__(self):
        info = super().__str__()
        return f'\nМашина. {info}'

    def tax(self):
        return 0.005 * self.worth


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def __str__(self):
        info = super().__str__()
        return f'\nДом. {info}'

    def tax(self):
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
