from django.urls import path
from login.views import *
from core.views import home


urlpatterns = [
    path('', entrar),
    path('home/', home)
]