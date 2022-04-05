import os


def gen_files_path(catalog: str, directory="C:\\") -> str:
    """
    Path generator

    :param catalog: catalog to find
    :param directory: star directory
    :type: str
    :return: all paths during generation
    :raise PermissionError:
    """
    try:
        for folder in os.listdir(directory):
            temp = os.path.join(directory, folder)
            if not os.path.isfile(temp):
                yield temp
                if folder == catalog:
                    return
                yield from gen_files_path(catalog, temp)
    except PermissionError:
        pass


if __name__ == '__main__':
    to_find = input('Введите нужный каталог: ')
    choice = int(input('Директория по умолчанию/Вручную - 0/1: '))

    if choice == 1:
        start = input('\nВведите директорию через пробел: ').split()
        start = os.path.abspath(os.sep.join(start))
        my_gen = gen_files_path(catalog=to_find, directory=start)
    else:
        print()
        my_gen = gen_files_path(catalog=to_find)

    for line in my_gen:
        print(line)
