class MyDict(dict):
    def get(self, key):
        for i_key in self.keys():  # TODO или так просто
                                   #  if i_key in self:
                                   #      return self[i_key]
                                   #  else:
                                   #      return 0

            if key == i_key:
                return i_key
        else:
            return 0


if __name__ == '__main__':
    dict_1 = MyDict()
    dict_1['A'] = 'B'
    print(dict_1.get('A'))
    print(dict_1.get('B'))
