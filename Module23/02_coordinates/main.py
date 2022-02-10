import random


def f1(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


with open('coordinates.txt', 'r') as file:
    for line in file:
        nums_list = line.split()
        try:
            res1 = f1(int(nums_list[0]), int(nums_list[1]))
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
        except ZeroDivisionError:
            print('Error: division by zero!')
        number = random.randint(0, 100)
        with open('result.txt', 'a') as file_2:
            my_list = sorted([res1, res2, number])
            file_2.write(f'{str(my_list[0])} {str(my_list[1])} {str(my_list[2])}' + '\n')
