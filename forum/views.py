from django.shortcuts import render, get_object_or_404


def index(request):
    return render(request, 'index/index.html')

def login_cadastro(request):
    return render(request, 'index/login_cadastro.html')
