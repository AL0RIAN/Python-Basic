class Person:
    """
    Базовый класс описывающий человека

    Args:
        __name (str): имя
        __surname (str): фамилия
        __age (int): возраст
    """
    def __init__(self, __name, __surname, __age):
        self.__name = __name
        self.__surname = __surname
        self.__age = __age

    def get_name(self):
        """
        Геттер, возвращающий имя

        :return: __age
        :rtype: str
        """
        return self.__name


class Employee(Person):
    """
    Дочерний класс, описывающий работника. Родитель: Person

    Args:
        __name (str): имя
        __surname (str): фамилия
        __age (int): возраст
    """
    def __init__(self, __name, __surname, __age):
        super().__init__(__name, __surname, __age)

    def __str__(self):
        return f'{self.get_name()}'

    def salary(self):
        """
        Метод для расчёта зарплаты. Пуст; нужен для наследования.
        """
        pass


class Manager(Employee):
    """
    Дочерний класс, описывающий менеджера. Родитель: Employee

    Args:
        __name (str): имя
        __surname (str): фамилия
        __age (int): возраст
    """
    def __init__(self, __name, __surname, __age):
        super().__init__(__name, __surname, __age)

    def __str__(self):
        info = super().__str__()
        return f'Менеджер - {info}. Заработок: {self.salary()}'

    def salary(self):
        """
        Метод для расчёта зарплаты менеджера.
        :rtype: float
        """
        return 13000.00


class Agent(Employee):
    """
    Дочерний класс, описывающий агента. Родитель: Employee

    Args:
        __name (str): имя
        __surname (str): фамилия
        __age (int): возраст
        sales (int): продажи
    """
    def __init__(self, __name, __surname, __age, sales):
        super().__init__(__name, __surname, __age)
        self.sales = sales

    def __str__(self):
        info = super().__str__()
        return f'Агент - {info}. Заработок: {self.salary()}'

    def salary(self):
        """
        Метод для расчёта зарплаты агента.
        :rtype: float
        """
        return 5000 + (0.05 * self.sales)


class Worker(Employee):
    """
    Дочерний класс, описывающий агента. Родитель: Employee

    Args:
        __name (str): имя
        __surname (str): фамилия
        __age (int): возраст
        hours (int): часы
    """
    def __init__(self, __name, __surname, __age, hours):
        super().__init__(__name, __surname, __age)
        self.hours = hours

    def __str__(self):
        info = super().__str__()
        return f'Рабочий - {info}. Заработок: {self.salary()}'

    def salary(self):
        """
        Метод для расчёта зарплаты рабочего.
        :rtype: float
        """
        return 100.00 * self.hours


if __name__ == '__main__':
    employees = [Manager('Том', 'Робенсон', 30), Manager('Вера', 'Джонсон', 29), Manager('Вера', 'Кожемяка', 34),
                 Agent('Давид', 'Соловьев', 40, 500), Agent('Джон', 'Киселев', 50, 100), Agent('Сон', 'Лу', 30, 300),
                 Worker('Кирилл', 'Солотопов', 18, 8), Worker('Андрей', 'Левицкий', 18, 12),
                 Worker('Тимофей', 'Раенко', 18, 8)]

    for human in employees:
        print(human)
