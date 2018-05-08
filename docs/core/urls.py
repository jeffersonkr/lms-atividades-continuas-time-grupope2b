from django.urls import path
from core.views import home, formulario



urlpatterns = [
    path('', home),
    path('ListaAprovacao/',formulario,),
]
