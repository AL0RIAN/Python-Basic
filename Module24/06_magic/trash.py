class Example_1:
    def __add__(self, other):
        if type(other) == Example_2:
            return Example_2()
        elif type(other) == Example_3:
            return Example_3()


class Example_2:
    answer = 'сложили два класса и вывели'


class Example_3:
    answer = 'сложили два класса и вывели!!!'


a = Example_1()
b = Example_3()
c = a + b
print(c.answer)
