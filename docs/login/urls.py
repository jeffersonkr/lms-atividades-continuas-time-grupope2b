from django.urls import path
from login.views import *



urlpatterns = [
    path('', entrar),
    path('sair/', sair)
]