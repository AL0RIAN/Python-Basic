class Person:
    def __init__(self, __name, __surname, __age):
        self.__name = __name
        self.__surname = __surname
        self.__age = __age

    def get_name(self):
        return self.__name


class Employee(Person):
    def __init__(self, __name, __surname, __age):
        super().__init__(__name, __surname, __age)

    def __str__(self):
        return f'{self.get_name()}'

    def salary(self):
        pass


class Manager(Employee):
    def __init__(self, __name, __surname, __age):
        super().__init__(__name, __surname, __age)

    def __str__(self):
        info = super().__str__()
        return f'Менеджер - {info}. Заработок: {self.salary()}'

    def salary(self):
        return 13000.00


class Agent(Employee):
    def __init__(self, __name, __surname, __age, sales):
        super().__init__(__name, __surname, __age)
        self.sales = sales

    def __str__(self):
        info = super().__str__()
        return f'Агент - {info}. Заработок: {self.salary()}'

    def salary(self):
        return 5000 + (0.05 * self.sales)


class Worker(Employee):
    def __init__(self, __name, __surname, __age, hours):
        super().__init__(__name, __surname, __age)
        self.hours = hours

    def __str__(self):
        info = super().__str__()
        return f'Рабочий - {info}. Заработок: {self.salary()}'

    def salary(self):
        return 100.00 * self.hours


if __name__ == '__main__':
    employees = [Manager('Том', 'Робенсон', 30), Manager('Вера', 'Джонсон', 29), Manager('Вера', 'Кожемяка', 34),
                 Agent('Давид', 'Соловьев', 40, 500), Agent('Джон', 'Киселев', 50, 100), Agent('Сон', 'Лу', 30, 300),
                 Worker('Кирилл', 'Солотопов', 18, 8), Worker('Андрей', 'Левицкий', 18, 12),
                 Worker('Тимофей', 'Раенко', 18, 8)]

    for human in employees:
        print(human)


