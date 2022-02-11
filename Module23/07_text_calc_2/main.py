def text_calc(operand1, sign, operand2):
    try:
        if sign == '+':
            return operand1 + operand2
        elif sign == '-':
            return operand1 - operand2
        elif sign == '*':
            return operand1 * operand2
        elif sign == '/':
            if operand1 != 0:
                return operand1 / operand2
            else:
                raise ZeroDivisionError
        else:
            print(f'Обнаружена ошибка в строке: {f"{operand1} {sign} {operand2}"}   Хотите исправить? ')
            choice = input().lower()
            if choice == 'да':
                correct = input('Введите исправленную строку: ')
                if text_calc(int(correct.split()[0]), correct.split()[1], int(correct.split()[2])):
                    print(text_calc(int(correct.split()[0]), correct.split()[1], int(correct.split()[2])))
            else:
                return False
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")


with open('calc.txt', 'r') as file:
    for line in file.readlines():
        if text_calc(int(line.split()[0]), line.split()[1], int(line.split()[2])):
            print(text_calc(int(line.split()[0]), line.split()[1], int(line.split()[2])))

