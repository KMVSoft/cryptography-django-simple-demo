from django.shortcuts import render

# Create your views here.

def main_menu(request):
    return render(request, 'index/menu.html', locals())