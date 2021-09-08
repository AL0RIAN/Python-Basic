def palindrom(num_list):
    reverse = []
    for i_num in range(len(num_list) - 1, -1, -1):
        reverse.append(num_list[i_num])
        return True if num_list == reverse else False


n = int(input('Кол-во чисел: '))
lst = []
new_nums = []
res = []

for index in range(n):
    print('Число:', index + 1, end=' ')
    number = int(input())
    lst.append(number)

for i_nums in range(0, len(lst)):
    for j_elem in range(i_nums, len(lst)):
        new_nums.append(lst[j_elem])

    if palindrom(new_nums):
        for i_answer in range(0, i_nums):
            res.append(lst[i_answer])
        res.reverse()
        break
    new_nums = []

print('\nПоследовательность:', lst)
print('Нужно приписать чисел:', len(res))
print('Сами числа::', res)
