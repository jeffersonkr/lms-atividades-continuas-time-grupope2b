from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.listarDisciplinas),
    path('incluir/', views.incluirDisciplinas),
    path('alterar/<int:id>', views.alterarDisciplinas),
    path('remover/<int:id>', views.removerDisciplina),

]
