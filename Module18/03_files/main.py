text = input('Название файла: ')

if text[0] in '@№$%^&*()':
    print('Ошибка: название начинается на один из специальных символов')
elif not text.endswith('.txt') and not text.endswith('.docx'):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно')
