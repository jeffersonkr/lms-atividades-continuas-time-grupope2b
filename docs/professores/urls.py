from django.urls import path
from professores.views import *

urlpatterns = [

    path('', areaProfessor),
    path('msgprofessor/', mensagemProfessor),
    path('principalprofessor/', subPrincioalProf)
    
]