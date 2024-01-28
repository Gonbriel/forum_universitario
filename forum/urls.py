from django.urls import path
from forum.views import index, login_cadastro

urlpatterns = [
    path('', index, name='index'),
    path('login_cadastro/', login_cadastro, name='login_cadastro'),
]
