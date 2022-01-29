file_first = open('first_tour.txt', 'r')

tour = {}
k = int(file_first.readline())

for member in file_first.readlines():
    member = member.split()
    if int(member[2]) > k:
        tour[member[0][0] + '.' + ' ' + member[1]] = int(member[2])

temp_score = 0
temp_member = ''
members = []
scores = []

while tour:
    for member in tour:
        if tour[member] > temp_score:
            temp_score = tour[member]
            temp_member = member
    scores.append(temp_score)
    members.append(temp_member)
    tour.pop(temp_member)
    temp_score = 0
    temp_member = ''

file_first.close()

file_second = open('second_tour.txt', 'w')

file_second.write(str(len(scores)) + '\n')

for winner in range(len(scores)):
    file_second.write('{}) {} {}\n'.format(winner + 1, members[winner], scores[winner]))

file_second.close()
