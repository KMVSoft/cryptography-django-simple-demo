from django.shortcuts import render
import ciphers.vigenere as vig
import  ciphers.transposition as trpos
import  ciphers.matrix as mtrx
import ciphers.gamma as gam
import re

# Create your views here.

def vigenere(request):
    result = ''
    error = ''
    re_key = re.compile("^[а-яА-ЯёЁ]+$")
    re_text = re.compile("^[а-яА-ЯёЁ .!,?\n\r]+$")
    if request.method == 'POST':
        action = request.POST.get('action')
        key = request.POST.get('key')
        text = request.POST.get('text')
        if not re_key.match(key):
            error = 'The value in the field "key" must consists only of Russian letters'
        elif not re_text.match(text):
            error = 'The value in the filed "text" must' \
                    ' consists only of Russian letters or spaces or punctuation marks'
        else:
            if action == 'Encrypt':
                result = vig.encrypt(key.lower(), text.lower())
            elif action == 'Decrypt':
                result = vig.decrypt(key.lower(), text.lower())
    return render(request, 'ciphers/vigenere.html', {'result': result, 'error': error})

def transposition(request):
    result = ''
    if request.method == 'POST':
        action = request.POST.get('action')
        key = request.POST.get('key')
        text = request.POST.get('text')
        if action == 'Encrypt':
            result = trpos.encrypt(key.lower(), text.lower())
        elif action == 'Decrypt':
            result = trpos.decrypt(key.lower(), text.lower())
    return render(request, 'ciphers/transposition.html', {'result': result})

def matrix(request):
    result = ''
    if request.method == 'POST':
        action = request.POST.get('action')
        text = request.POST.get('text')
        matr = [
            [int(request.POST.get('1_1')), int(request.POST.get('1_2')), int(request.POST.get('1_3')), int(request.POST.get('1_4'))],
            [int(request.POST.get('2_1')), int(request.POST.get('2_2')), int(request.POST.get('2_3')), int(request.POST.get('2_4'))],
            [int(request.POST.get('3_1')), int(request.POST.get('3_2')), int(request.POST.get('3_3')), int(request.POST.get('3_4'))],
            [int(request.POST.get('4_1')), int(request.POST.get('4_2')), int(request.POST.get('4_3')), int(request.POST.get('4_4'))]
        ]
        if action == 'Encrypt':
            result = mtrx.encrypt(text.lower(), matr)
        elif action == 'Decrypt':
            result = mtrx.decrypt(text.lower(), matr)
    return render(request, 'ciphers/matrix.html', {'result': result})


def gamma(request):
    result = ''
    error = ''
    re_text = re.compile("^[а-яА-ЯёЁ .!:\-–,?\n\r]+$")
    if request.method == 'POST':
        action = request.POST.get('action')
        key = request.POST.get('key')
        text = request.POST.get('text')
        if not re_text.match(text):
            error = 'The value in the filed "text" must' \
                    ' consists only of Russian letters or spaces or punctuation marks'
        else:
            if action == 'Gamma':
                if key:
                    result = gam.gamma(text, [int(x) for x in key.split()])
                else:
                    result = gam.gamma(text)
    return render(request, 'ciphers/gamma.html', {'result': result, 'error': error})