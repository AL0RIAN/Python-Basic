sum = 0
file = open("numbers.txt", "r")

for sym in file.read():
    if sym.isdigit():
        sum += int(sym)
file.close()

file = open("answer.txt", "w")
file.write(str(sum))
file.close()
