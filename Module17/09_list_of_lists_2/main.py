nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
res = [number for lst in nice_list for lst2 in lst for number in lst2]
print('Результат:', res)

# first = [number for lst in nice_list[0] for number in lst]
# second = [number for lst in nice_list[1] for number in lst]
# first.extend(second)
