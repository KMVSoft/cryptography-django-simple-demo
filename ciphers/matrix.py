import numpy as np

def encrypt(text, matr):
    text = text.replace('\r', '').replace('\n', '')
    # дополнение строки до кратной 4-м
    text += ' ' * (4 - len(text) % 4)
    data = quartering(str_to_int(text))
    multiply_matrix(data, np.array(matr))
    return int_to_str(unquartering(data))

def decrypt(text, matr):
    data = quartering(str_to_int(text))
    multiply_matrix(data, np.linalg.inv(np.array(matr)))
    return int_to_str(unquartering(data))


def str_to_int(text):
    # строку в массив чисел
    res = []
    for i in text:
        res.append(ord(i))
    return res

def int_to_str(lst):
    # массив чисел в строку
    res = ''
    for i in lst:
        res += chr(int(round(i)))
    return res

def quartering(lst):
    # четвертование списка на список с векторами размера 4
    res = []
    quadriada = []
    for e in lst:
        quadriada.append(e)
        if len(quadriada) == 4:
            res.append(np.array(quadriada))
            quadriada = []
    return res

def unquartering(lst):
    # дизчетвертование списка на список с векторами размера 4
    res = []
    for quad in lst:
        for e in quad:
            res.append(e)
    return res

def multiply_matrix(lst, mtrx):
    # умножение матрицы на список векторов
    for i in range(len(lst)):
        lst[i] = mtrx.dot(lst[i])