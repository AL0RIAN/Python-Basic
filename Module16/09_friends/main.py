n = int(input('Кол-во друзей: '))
k = int(input('Кол-во долговых расписок: '))
money = []

for _ in range(n):
    money.append(0)

for receipt in range(k):
    print()
    print(receipt + 1, 'расписка')
    debtor = int(input('Кому: '))
    creditor = int(input('От кого: '))
    how_money = int(input('Сколько: '))
    money[debtor - 1] -= how_money
    money[creditor - 1] += how_money

print('\nБаланс друзей:')
for friend in range(n):
    print(friend + 1, ':', money[friend])
