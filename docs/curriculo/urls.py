from django.urls import path
from curriculo.views import listarDisciplinas, incluirDisciplinas, alterarDisciplinas

urlpatterns = [

    path('', listarDisciplinas),
    path('incluir/', incluirDisciplinas),
    path('alterar/<int:id>', alterarDisciplinas),
]