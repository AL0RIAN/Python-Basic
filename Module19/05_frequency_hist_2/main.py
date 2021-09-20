text = 'Здесь что-то написано'
frequency = {symbol: text.count(symbol) for symbol in text}

for key in frequency:
    print('{0} : {1}'.format(key, frequency[key]))
print()

result = []
for index in range(1, max(frequency.values()) + 1):
    for key in frequency:
        if frequency[key] == index:
            result.append(key)
    print('{0} : {1}'.format(index, result))
    result = []
