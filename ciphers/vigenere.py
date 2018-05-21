import re
LETTERS_NUM_RUS = 33 #number of letters in the Russian alphabet
CODE_FIRST_LETTER_RUS = 1072 #in utf-16be russian letter a has code 1072
RE_RUSSIAN = re.compile("^[а-яА-ЯёЁ]+$")

def shift(l, n):
    return l[n:] + l[:n]

def generate_russian_alphabet():
    alphabet = [chr(CODE_FIRST_LETTER_RUS + i % (LETTERS_NUM_RUS-1)) for i in range(0, LETTERS_NUM_RUS-1)]
    alphabet.insert(6, 'ё')
    return alphabet

def generate_vigenere_table_rus():
    a = generate_russian_alphabet()
    return [shift(a, i) for i in range(0, LETTERS_NUM_RUS)]

def encrypt(key, text):
    vigenere_table = generate_vigenere_table_rus()
    alphabet = generate_russian_alphabet()
    result = ''
    omit = 0
    for i in range(0, len(text)):
        if RE_RUSSIAN.match(text[i]):
            k_index = (i - omit) % len(key)
            row_index = alphabet.index(key[k_index])
            column = vigenere_table[row_index]
            col_index = alphabet.index(text[i])
            result += column[col_index]
        else:
            result += text[i]
            omit += 1
    return result

def decrypt(key, text):
    vigenere_table = generate_vigenere_table_rus()
    alphabet = generate_russian_alphabet()
    result = ''
    omit = 0
    for i in range(0, len(text)):
        if RE_RUSSIAN.match(text[i]):
            k_index = (i - omit) % len(key)
            row_index = alphabet.index(key[k_index])
            column = vigenere_table[row_index]
            alphabet_index = column.index(text[i])
            result += alphabet[alphabet_index]
        else:
            result += text[i]
            omit += 1
    return result