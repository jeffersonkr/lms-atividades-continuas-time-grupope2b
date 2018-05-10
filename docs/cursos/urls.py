from django.urls import path
from cursos.views import *

urlpatterns = [

    path('', listaCursos),
    path('incluir/', incluirCurso),
    path('alterar/<int:id>', alterarCurso),
    path('novoCurso/', listaCursos),
    path('remover/<int:id>', removerCurso),
]