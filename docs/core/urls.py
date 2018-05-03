from django.urls import path
from core.views import home, formulario, cadastroAluno



urlpatterns = [
    path('', home),
    path('ListaAprovacao/',formulario,),
    path('cadAluno/',cadastroAluno),
]
