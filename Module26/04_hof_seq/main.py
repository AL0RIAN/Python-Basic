class QHofstadter:
    def __init__(self, lst: list) -> None:
        if lst != [1, 1]:
            raise KeyError
        self.lst = lst

    def __iter__(self) -> any:
        return self

    def __next__(self) -> int:
        try:
            res = self.lst[-self.lst[-1]] + self.lst[-self.lst[-2]]
            self.lst.append(res)
            return res
        except IndexError:
            raise StopIteration()


if __name__ == '__main__':
    Q = QHofstadter([1, 1])
    while True:
        choice = int(input('1 - следующий элемент\n2 - вывести текущие элементы\n3 - выход из цикла\nВвод: '))
        if choice == 1:
            print(f'\nСледующий элемент: {next(Q)}\n')
        elif choice == 2:
            print(f'\nВесь список: {Q.lst}\n')
        elif choice == 3:
            print('\nКонец программы')
            break
        else:
            raise KeyError
