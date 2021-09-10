vowel = ["у", "а", "о", "я", "ю", "э", "ы", "е", 'ё', "и", "И", "У", "А", "О", "Я", "Ю", "Э", "Ы", "Е", 'Ё']
text = input('Введите текст (на русском): ')
vowel_in_text = [letter for letter in text if letter in vowel]

print('\nСписок гласных букв:', vowel_in_text)
print('Длина списка:', len(vowel_in_text))