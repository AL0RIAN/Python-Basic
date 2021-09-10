n = [1, 0, 2, 0, 3, 0, 4, 0, 5, 0, 6, 0]
zero = [zero for zero in n if zero == 0]
non_zero = [number for number in n if number != 0]
non_zero.extend(zero)
print(non_zero)
print(non_zero[:non_zero.index(0)])