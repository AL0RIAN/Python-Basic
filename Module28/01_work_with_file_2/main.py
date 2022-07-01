from typing import TextIO


class File:
    """ Класс контекст-менеджер, открывающий файл в заданном режиме и обрабатывающий ошибки """

    def __init__(self, name: str, mode: str) -> None:
        """
        :param str name: имя файла
        :param str mode: режим открытия файла
        """
        self.name = name
        self.mode = mode

    def __enter__(self) -> TextIO:
        """
        :return: возвращает открытый файл

        Обрабатывает исключение FileNotFoundError. В случае ошибки открывает файл в режиме записи.
        """
        try:
            self.file = open(self.name, self.mode)
        except FileNotFoundError:
            self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        """
        :return: True

        Закрывает файл
        """
        self.file.close()
        return True


if __name__ == "__main__":
    with File("text.txt", "r") as file:
        try:
            print(file.readline())
        except Exception:
            file.write("ABCD")
