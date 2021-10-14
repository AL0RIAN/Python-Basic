n = int(input("Кол-во строк протокола: "))
lst = {}

for index in range(n):
    print(f"{index + 1} запись:", end=' ')
    score, member = input().split()
    score = int(score)
    if member in lst.keys():
        if lst[member] < score:
            lst[member] = score
        else:
            pass
    else:
        lst[member] = score
print()

scores = sorted(lst.values())

for position in range(3):
    for winner in lst.keys():
        if lst[winner] == scores[-1]:
            print("{0} место. {1} ({2})".format(position + 1, winner, scores[-1]))
            scores.pop()
            break
