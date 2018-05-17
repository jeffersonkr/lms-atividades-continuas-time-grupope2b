from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('alunos/', views.listarAluno),
    path('alunos/cadastroaluno/', views.cadastroAluno),
    path('alunos/alterar/<int:id>', views.alterarAluno),
    path('alunos/remover/<int:id>', views.removerAluno),
    path('professores/', views.listaProfessor),
    path('professores/cadastrarProfessor/', views.cadastrarProfessor),
    path('professores/alterar/<int:id>', views.alterarProfessor),
    path('professores/remover/<int:id>', views.removerProfessor),
]