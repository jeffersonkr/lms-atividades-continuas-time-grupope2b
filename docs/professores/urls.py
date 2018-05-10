from django.urls import path
from professores.views import listaProfessor, cadastrarProfessor

urlpatterns = [

    path('', listaProfessor),
    path('cadastrarProfessor/', cadastrarProfessor)
    
]