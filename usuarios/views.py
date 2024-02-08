from django.shortcuts import render, get_object_or_404

def login_cadastro(request):
    return render(request, 'usuarios/login_cadastro.html')