from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.indexAlunos),
    path('cadastroaluno/', views.cadastroAluno),
    path('alterar/<int:id>', views.alterarAluno),
    path('remover/<int:id>', views.removerAluno),
    path('areadoaluno/', views.areaDoAluno),
    path('areadoaluno/mensagens/', views.mensagensAluno),
    path('areadoaluno/principal/', views.subPrincipal),
]