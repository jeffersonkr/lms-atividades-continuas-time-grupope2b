from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.indexAlunos),
    path('mensagens/', views.mensagensAluno),
    path('principal/', views.subPrincipal),
]