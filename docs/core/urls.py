from django.urls import path
from core.views import *



urlpatterns = [
    path('', home),
    path('graduacao/', graduacao),
    path('ads/', ads),
    path('bd/', bd),
    path('gti/', gti),
    path('jogosdigitais/', jogosdigitais),
    path('administracao/', adm),
]
