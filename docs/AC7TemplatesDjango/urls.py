"""AC7TemplatesDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core.views import home, formulario, listaCursos, cadastroAluno, detalheCurso
from utils.views import media
from curriculo.views import listaCursos2, curso, incluirCurso, alterarCurso, listarDisciplinas, incluirDisciplinas, alterarDisciplinas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('ListaAprovacao/',formulario,),
    path('Lista/',listaCursos),
    path('cadAluno/',cadastroAluno),
    path('curso/ads',detalheCurso),
    path('media/', media),
    #path('cursos/<str:sigla>',curso),
    path('novoCurso/', listaCursos2),
    path('cursos/incluir/', incluirCurso),
    path('cursos/alterar/<int:id>', alterarCurso),

    path('Disciplinas/', listarDisciplinas),
    path('Disciplinas/incluir/', incluirDisciplinas),
    path('Disciplinas/alterar/<int:id>', alterarDisciplinas),
]
