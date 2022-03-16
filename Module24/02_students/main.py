from random import randint


class Student:

    def __init__(self, name, surname, marks, group):
        self.name = name
        self.surname = surname
        self.marks = marks
        self.group = group

    def get_info(self):
        print(f'Имя и фамилия: {self.name} {self.surname}')
        print(f'Номер группы: {self.group}')
        print(f'Оценки: {self.marks}')

    def gpa(self):
        return sum(self.marks) / len(self.marks)


if __name__ == "__main__":
    with open('names.txt', 'r') as name_file:
        names = [name.rstrip() for name in name_file.readlines()]
    with open('surnames.txt', 'r') as surname_file:
        surnames = [surname.rstrip() for surname in surname_file.readlines()]

    students = [Student(names[randint(0, 999)],
                        surnames[randint(0, 49)],
                        [randint(1, 100) for mark in range(5)],
                        randint(1, 3)) for _ in range(10)]
    result = sorted([students[mark].gpa() for mark in range(10)], reverse=True)

    for mark in range(10):
        for student in range(10):
            if result[mark] == students[student].gpa():
                students[student].get_info()
                print('GPA:', students[student].gpa(), '\n')
                break
