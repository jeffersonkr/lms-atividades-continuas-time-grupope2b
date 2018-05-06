from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.listarDisciplinas),
    path('disciplinas/incluir/', views.incluirDisciplinas),
    path('disciplinas/alterar/', views.alterarDisciplinas),

]
