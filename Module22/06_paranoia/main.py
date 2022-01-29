def caesar_cipher(word, step):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_word = ''
    for letter in word:
        if letter != '\n':
            new_word += (alphabet[(alphabet.index(letter.lower()) + step) % 25])
        else:
            break
    return new_word


count = 1
text_file = open('text.txt', 'r')
cipher_file = open('cipher_text.txt', 'w')

for line in text_file.readlines():
    cipher_file.write(caesar_cipher(line, count) + '\n')
    count += 1

text_file.close()
cipher_file.close()
