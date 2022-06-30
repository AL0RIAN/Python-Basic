class Date:
    """ Класс, описывающий дату """
    def __init__(self, day, month, year):
        """
        :param day: день
        :param month: месяц
        :param year: год
        """
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"День: {self.day}\t\tМесяц: {self.month}\t\tГод: {self.year}"

    @classmethod
    def correct(cls, date: str) -> bool:
        """
        Статический метод, который проверяет корректность записи даты

        :param date: дата в формате dd.mm.yyyy
        :return: True, если дата записана корректно, False - если в записи ошибка
        """
        temp = date.split("-")
        if not (temp[0].isdigit() and temp[1].isdigit() and temp[2].isdigit()):
            return False
        elif not (1 <= int(temp[0]) <= 31):
            return False
        elif not (1 <= int(temp[1]) <= 12):
            return False
        elif not (int(temp[2]) > 0):
            return False
        else:
            return True

    @classmethod
    def converter(cls, date: str) -> 'Date':
        """
        Статический метод, разбивающий дату формата dd.mm.yyyy на поля экземпляра класса Date

        :param date: дата в формате dd.mm.yyyy
        :return: экземпляр класса Date
        """
        temp = date.split("-")
        return Date(temp[0], temp[1], temp[2])


if __name__ == "__main__":
    date = Date.converter(date='10-12-2077')
    print(date)
    print(date.correct(date='10-12-2077'))
    print(date.correct(date='40-12-2077'))
