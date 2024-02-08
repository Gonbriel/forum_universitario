from django.urls import path
from usuarios.views import login_cadastro

urlpatterns = [
    path('login_cadastro/', login_cadastro, name='login_cadastro'),
]