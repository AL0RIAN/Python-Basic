def tuple_sort(tuple_):
    lst = []
    for item in tuple_:
        if str(item).isdigit():
            lst.append(item)
        else:
            return tuple_
    return tuple(sorted(lst))


original = (5, 6, 7, 2, 2, 8, 9, 10, 1)
print(tuple_sort(original))

