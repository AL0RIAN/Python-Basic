first = list(range(160, 177, 2))
second = list(range(162, 181, 3))

first.extend(second)

for _ in range(len(first) - 1):
    flag = 0
    for index in range(0, len(first) - 1):
        if first[index] > first[index + 1]:
            a = first[index]
            b = first[index + 1]
            first[index] = b
            first[index + 1] = a
            flag = 1
    if flag == 0:
        break

print(first)
