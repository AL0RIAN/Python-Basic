def shortest(str, tpl):
    return min(len(str), len(tpl))


text = [1], [2], [3], [4]
numbers = [[1, ], (1), {1: 2}]

new = ((text[i], numbers[i]) for i in range(shortest(text, numbers)))
print(new)

for i in new:
    print(i)
