def sum_of_number(n):
    summa = 0
    while n != 0:
        summa = n % 10
        n //= 10
    print('Сумма цифр:', summa)
    return summa


def count_of_number(n):
    count = 0
    while n != 0:
        count += 1
        n //= 10
    print('Кол-во цифр в числе:', count)
    return count


n = int(input('Число: '))
print('Разность суммы и кол-ва цифр:', sum_of_number(n) - count_of_number(n))
