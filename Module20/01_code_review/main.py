def vanya_revenge(dict):
    lst = [interest for key, item in dict.items() for interest in item['interests']]
    surnames = [surname for key, item in dict.items() for surname in item['surname']]
    return lst, len(surnames)


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

result = vanya_revenge(students)
print("Result: {0}, {1}".format(result[0], result[1]))
