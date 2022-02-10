def text_calc(operand1, sign, operand2):
    if sign == '+':
        return operand1 + operand2
    elif sign == '-':
        return operand1 - operand2
    elif sign == '*':
        return operand1 * operand2
    elif sign == '/':
        try:
            if operand1 != 0:
                return operand1 / operand2
            else:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print("Ошибка: деление на ноль!")
    else:
        return False


with open('calc.txt', 'r') as file:
    for line in file.readlines():
        if text_calc(int(line.split()[0]), line.split()[1], int(line.split()[2])):
            print(text_calc(int(line.split()[0]), line.split()[1], int(line.split()[2])))
