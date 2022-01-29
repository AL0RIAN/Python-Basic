letters = {}
total = 0

file_text = open('text.txt', 'r')
for letter in file_text.read():
    if letter.isalpha():
        total += 1
        if letter.lower() in letters:
            letters[letter.lower()] += 1
        else:
            letters[letter.lower()] = 1

temp_score = 0
temp_member = ''
members = []
count = []

while letters:
    for sym in sorted(letters):
        if letters[sym] > temp_score:
            temp_score = letters[sym]
            temp_member = sym
    count.append(temp_score)
    members.append(temp_member)
    letters.pop(temp_member)
    temp_score = 0
    temp_member = ''

file_text.close()

file_analysis = open('analysis.txt', 'w')
for elem in range(len(members)):
    file_analysis.write('{} {:.3f}'.format(members[elem], (count[elem] / total)) + '\n')
file_analysis.close()
