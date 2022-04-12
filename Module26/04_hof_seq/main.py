class QHofstadter:
    def __init__(self, lst: list) -> None:
        # TODO тут надо проверить lst на валидность (равенство списку [1, 1]) и если он не валидный, то выбросить
        #  исключение
        self.lst = lst

    def __iter__(self) -> any:
        return self

    def __next__(self) -> int:
        try:
            q1 = self.lst[-1]
            q2 = self.lst[-2]
            # TODO на самом деле формула немного сложнее: Q(n) = Q(n − Q(n − 1)) + Q(n − Q(n − 2))
            self.lst.append(q1 + q2)
            return q1 + q2
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
