import math


class MyMath:
    """ Класс для расчетов математических величин """

    @classmethod
    def circle_len(cls, radius: int) -> float:
        """
        :param int radius: радиус окружности
        :return float: длина окружности

        Формула: 2πR
        """
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: int) -> float:
        """
        :param int radius: радиус окружности
        :return float: площадь поверхности сферы

        Формула: πr^2
        """
        return math.pi * radius ** 2

    @classmethod
    def cube_vol(cls, edge: int) -> int:
        """
        :param int edge: ребро куба
        :return float: объем куба

        Формула: a^3
        """
        return edge ** 3

    @classmethod
    def sphere_sq(cls, radius: int) -> float:
        """
        :param int edge: ребро куба
        :return float: объем куба

        Формула: 4πR^2
        """
        return math.pi * 4 * radius ** 2


if __name__ == "__main__":
    res_1 = MyMath.circle_len(radius=5)
    res_2 = MyMath.circle_sq(radius=6)
    res_3 = MyMath.cube_vol(edge=3)
    res_4 = MyMath.sphere_sq(radius=4)

    print(res_1)
    print(res_2)
    print(res_3)
    print(res_4)
