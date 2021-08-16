def special_year(a, b):
    for year in range(a, b + 1):
        for number in str(year):
            if str(year).count(number) == 3:
                print(year)
                break


a = int(input('Первый год: '))
b = int(input('Второй год: '))
special_year(a, b)
