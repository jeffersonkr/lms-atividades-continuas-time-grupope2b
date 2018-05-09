from django.urls import path
from login.views import novoUsuario, listaUsuarios, login


urlpatterns = [

    path('', login),
    path('novoUsuario/', novoUsuario),
    path('listaUsuarios/', listaUsuarios)

]