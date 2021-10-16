def shortest(str, tpl):
    return min(len(str), len(tpl))


text = 'abcdfc'
numbers = (10, 20, 30, 40)

new = ((text[i], numbers[i]) for i in range(shortest(text, numbers)))
print(new)
for item in new:
    print(item)
