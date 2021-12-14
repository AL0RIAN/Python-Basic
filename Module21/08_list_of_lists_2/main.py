def straight(struct, new=[]):
    for value in struct:
        if isinstance(value, list):
            straight(value)
        else:
            new.append(value)
    return new                               


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print('Ответ:', straight(nice_list))
