import os


def comment_check(string: str) -> bool:
    """
    Checking for a comment in a line

    :param string: string to comment check
    :return: False or True
    """
    for sym in string:
        if sym.isalpha() or sym.isdigit():
            return False
        elif sym == '#':
            return True


def my_gen(direct: str) -> list:
    """
    Generator to count the number of lines in files (.py)
    """
    count = 0
    for obj in os.listdir(direct):
        if os.path.isdir(os.path.join(direct, obj)):
            yield from my_gen(os.path.join(direct, obj))
        if obj.endswith('.py'):
            obj_1 = os.path.join(direct, obj)
            with open(obj_1, 'r', encoding='utf-8') as file:
                for line in file.readlines():
                    if not line.isspace() and not comment_check(line):
                        count += 1
                        yield count
                        print(line, end='')


if __name__ == '__main__':
    directory = input('Введите через пробел директорию: ').split()
    directory = os.sep.join(directory)

    for i_line in my_gen(direct=directory):
        print(i_line, end=' ')
