from django.shortcuts import render

def login_cadastro(request):
    return render(request, 'usuarios/login_cadastro.html')