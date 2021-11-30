def func(tpl, elem):
    interval = [index for index, item in enumerate(tpl) if item == elem]
    if tpl.count(elem) == 2:
        return tpl[interval[0]:interval[1] + 1]
    elif tpl.count(elem) == 1:
        return tpl[interval[0]:]
    else:
        return ()


numbers = (1, 1, 0, 1, 2, 3, 4, 0, 1, 1)
print(func(numbers, 0))

