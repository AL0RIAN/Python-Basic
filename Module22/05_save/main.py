import os


def write_file(path_name, data):
    file = open(path_name, "w")
    file.write(data)
    file.close()


text = input('Введите строку: ')

seq_folders = (input("Куда хотите сохранить документ? Введите последовательность папок (через пробел):\n")).split()
path = os.path.join('C:', os.sep, '')
for word in seq_folders:
    path = os.path.join(path, word)
print()

file_name = input('Введите имя файла: ')

if os.path.exists(path):
    path = os.path.join(path, file_name + '.txt')
    if os.path.exists(path):
        choice = input('Вы действительно хотите перезаписать файл? ').lower()
        if choice == 'да':
            write_file(path, text)
            print('Файл успешно перезаписан!')
        else:
            print('Отмена перезаписи файла')
    else:
        write_file(path, text)
        print('Файл успешно перезаписан!')
else:
    print('Ошибка! Такого пути не существует!')
