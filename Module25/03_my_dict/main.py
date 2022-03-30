class MyDict(dict):
    """
    Дочерний класс dict
    """

    def get(self, key):
        """
        Ф-я поиска ключа в словаре

        :param key: ключ, который нужно найти в self
        :type: любой неизменяемый тип
        :return: self[key], если ключ находится в словаре, иначе 0
        """
        if key in self:
            return self[key]
        else:
            return 0


if __name__ == '__main__':
    dict_1 = MyDict()
    dict_1['A'] = 'B'
    print(dict_1.get('A'))
    print(dict_1.get('B'))
