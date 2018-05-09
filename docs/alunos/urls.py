from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.indexAlunos),
    path('cadastroaluno/', views.cadastroAluno)
]