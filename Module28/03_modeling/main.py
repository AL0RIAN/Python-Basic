import random
from random import randint
import math


class Triangle:
    """ Класс описывающий треугольник """

    def __init__(self, base: float, height: float) -> None:
        """
        :param base: основание треугольника
        :param height: высота треугольника
        """

        self.base = base
        self.height = height

    def t_area(self) -> float:
        """ :return float: площадь треугольника """
        return 1 / 2 * self.base * self.height

    def t_perimetr(self) -> float:
        """ :return float: периметр треугольника """
        side = math.sqrt((self.base / 2) ** 2 + self.height ** 2)
        return self.base + 2 * side


class Square:
    def __init__(self, side: float) -> None:
        """
        :param side: сторона квадрата
        """
        self.side = side

    def sq_area(self) -> float:
        """
        :return float: площадь квадрата
        """
        return self.side ** 2

    def sq_perimetr(self) -> float:
        """
        :return float: периметр квадрата
        """
        return 4 * self.side


class Pyramid:
    def __init__(self, base: Square, sides: list) -> None:
        """
        :param sides: стороны пирамиды, где 0-й индекс - основание
        """
        self.base = base
        self.sides = sides

    def pyramid_area(self) -> float:
        """
        :return float: площадь боковой поверхности
        """
        return (self.base.sq_perimetr() * self.sides[0].height) / 2 # по апофеме и периметру основания


class Cube:
    def __init__(self, edges: list) -> None:
        """
        :param edges: ребра куба
        """
        self.edges = edges

    def cube_area(self) -> int:
        """
        :return: площадь поверхности
        """
        res = 0
        for sq in self.edges:
            temp = sq.sq_area()
            res += temp
        return res


if __name__ == "__main__":
    cube = Cube(edges=[Square(side=randint(2, 10)) for _ in range(6)])
    print(cube.cube_area())

    pyramid = Pyramid(base=Square(3), sides=[Triangle(base=randint(2, 10), height=randint(2, 10)) for _ in range(4)])
    print(pyramid.pyramid_area())
