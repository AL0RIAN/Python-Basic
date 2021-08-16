def least_divisor(n):
    for number in range(2, n + 1):
        if n % number == 0:
            return number


n = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', least_divisor(n))
