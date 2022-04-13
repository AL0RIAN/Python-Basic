def finder(number: int, first: list, second: list) -> str:
    """

    :param number: the number to be found
    :param first: fist list of numbers
    :param second: second list of numbers
    """
    for x in first:
        for y in second:
            yield f'{x} * {y} == {x * y}'
            if x * y == to_find:
                print('Found!!')
                return


if __name__ == '__main__':
    list_1 = [2, 5, 7, 10]
    list_2 = [3, 8, 4, 9]
    to_find = 56

    for i_num in finder(number=to_find, first=list_1, second=list_2):
        print(i_num)
