import math


def is_prime(item_index):
    for number in range(2, int(math.sqrt(item_index) + 1)):
        if item_index % number == 0:
            return False
    return True


def universal_program(iter_item):
    return [item for index, item in enumerate(iter_item) if is_prime(index) and index != 0]


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(universal_program(lst))
