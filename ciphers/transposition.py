


def encrypt(key, text):
    text += ' ' * (len(key) - len(text) % len(key))
    table = generate_table(key)
    fillin_text(table, key, text)
    table = sort_table(table)
    return pourout_text(table, key, text)

def decrypt(key, text):
    table = generate_table(key)
    table = sort_table(table)
    text += ' ' * (len(key) - len(text) % len(key))
    fillin_text(table, key, text)
    unsort_table(table, key)
    return pourout_text(table, key, text)


def generate_table(key):
    return [[i] for i in key]

def fillin_text(table, key, text):
    for i in range(0, len(text)):
        table[i % len(key)].append(text[i])

def pourout_text(table, key, text):
    result = ''
    for i in range(0, len(text)):
        result += table[i % len(key)][1+i // len(key)]
    return result

def sort_table(table):
    return sorted(table, key=lambda x: x[0])

def unsort_table(table, key):
    for i in range(len(key)):
        for j in range(i, len(key)):
            if key[i] == table[j][0]:
                table[i], table[j] = table[j], table[i]