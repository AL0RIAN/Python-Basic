class SquareIter:
    """
    Iterator class for counting the squares of a numbers

    Args:
        maximum (int): maximum number of iteration
    """
    def __init__(self, maximum: int) -> None:
        self.maximum = maximum

    def __iter__(self) -> any:
        self.__minimum = 0
        return self

    def __next__(self) -> str:
        self.__minimum += 1
        if self.__minimum <= self.maximum:
            return f'{self.__minimum} ** 2 = {self.__minimum ** 2}'
        else:
            raise StopIteration


def square(maximum: int) -> str:
    """
    Generator function for counting the squares of a numbers

    :param maximum: maximum number of generation
    :return: square number
    """
    for minimum in range(1, maximum + 1):
        yield f'{minimum} ** 2 = {minimum ** 2}'


if __name__ == '__main__':
    number = int(input('Введите максимальное число: '))
    my_iter = SquareIter(number)
    for i_num in my_iter:
        print(i_num)

    print()

    for i_num in square(number):
        print(i_num)

    print()

    square_gen = (f'{minimum} ** 2 = {minimum ** 2}' for minimum in range(1, number + 1))

    for i_num in square_gen:
        print(i_num)
