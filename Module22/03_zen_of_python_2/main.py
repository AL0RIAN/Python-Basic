import os

file = open(os.path.abspath(os.path.join("..", "02_zen_of_python", "zen.txt")), "r")
letters = 0
words = 0
lines = 0
rarest_letter = {}

for letter in file.read():
    letters += len(letter)

file.seek(0)

for word in file.readlines():
    words += len(word.split(' '))

file.seek(0)

for line in file.readlines():
    lines += 1

file.seek(0)

for sym in file.read():
    if sym in rarest_letter:
        rarest_letter[sym.lower()] += 1
    else:
        if sym.isalpha():
            rarest_letter[sym.lower()] = 1

file.close()

print(rarest_letter)

print("Буквы:", letters)
print("Слова:", words)
print("Строки:", lines)
print("Самая редкая буква в тексте:", end=' ')

min_value = max(rarest_letter.values())
rarest_key = 0
for letter in rarest_letter:
    if rarest_letter[letter] < min_value:
        rarest_key = letter
        min_value = rarest_letter[letter]
print(rarest_key)
