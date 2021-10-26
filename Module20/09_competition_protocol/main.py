n = int(input("Кол-во строк протокола: "))
lst = {}
members = []

for index in range(n):
    print(f"{index + 1} запись:", end=' ')
    score, member = input().split()
    score = int(score)
    if member in lst.keys():
        if lst[member] < score:
            members.pop(members.index(member))
            members.append(member)
            lst[member] = score
    else:
        lst[member] = score
        members.append(member)
print()

scores = sorted(lst.values())

for position in range(3):
    for winner in members:
        if lst[winner] == scores[-1]:
            print("{0} место. {1} ({2})".format(position + 1, lst[winner], winner))
            members.pop(members.index(winner))
            scores.pop()
            break
