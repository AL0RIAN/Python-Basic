import itertools

numbers = list(range(0, 10))
count = 1

for item in itertools.combinations(numbers, 4):
    # TODO Только метод product обеспечивает полный перебор с повторами
    print(f'Вариант {count}: {" ".join(list(map(lambda x: str(x), item)))}')
    count += 1
