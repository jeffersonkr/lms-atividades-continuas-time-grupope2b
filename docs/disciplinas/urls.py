from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.listarDisciplinas),
    path('incluir/', views.incluirDisciplinas),
    path('alterar/', views.alterarDisciplinas),
    path('novaDisciplina/', views.listarDisciplinas),

]
