from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.listacoordenador),
    path('incluir/', views.incluirCoordenador),
    path('alterar/<int:id>', views.alterarCoordernador),
    path('remover/<int:id>', views.removerCoordenador),
]