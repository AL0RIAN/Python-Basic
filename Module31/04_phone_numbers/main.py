import re

pattern = r'[89]\d{9}'
temp = ['9999999999', '999999-999', '99999x9999']
index = 1

for number in temp:
    result = re.match(pattern, number)
    if result:
        print(f'{index} номер: всё в порядке')
    else:
        print(f'{index} номер: не подходит')
    index += 1
