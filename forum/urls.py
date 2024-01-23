from django.urls import path, include
from forum.views import index

urlpatterns = [
    path('', index, name='index'),
]
