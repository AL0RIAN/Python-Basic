count = 0
file = open("zen.txt", 'r')
count = 1
temp = 19
while temp:
    for line in file.readlines():
        if count == temp:
            if '\n' not in line:
                line += '\n'
            print(line, end='')
        count += 1
    count = 1
    temp -= 1
    file.seek(0)
