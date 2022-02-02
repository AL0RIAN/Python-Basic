def fib_pos(num_pos):
    if num_pos == 1 or num_pos == 2:
        return 1
    else:
        return fib_pos(num_pos - 1) + fib_pos(num_pos - 2)


position = int(input("Введите позицию числа в ряде Фибоначчи: "))
print(fib_pos(position))
