from django.urls import path
from cursos.views import listaCursos, incluirCurso, alterarCurso

urlpatterns = [

    path('', listaCursos),
    path('incluir/', incluirCurso),
    path('alterar/<int:id>', alterarCurso),
    path('novoCurso/', listaCursos),
]