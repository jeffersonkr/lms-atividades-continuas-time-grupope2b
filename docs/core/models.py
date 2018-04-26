from django.contrib.auth.models import professor
from django.db import models

class Professor:
    def __init__(self, nome='', email='', ra='', celular=''):
        self.__nome = nome
        self.__email = email
        self.__ra = ra
        self.__celular = celular
        
    
    def retornaSobrenome(self):
        return ' '.join(self.__nome.split(' ')[1:])    
        
    def retornaCargaHoraria(self):
        soma_carga = 0
        for d in self.__disciplinas:
            soma_carga += d.getCargaHoraria()
        return (soma_carga/20)*5


class Aluno:
    
    def __init__(self, nome='', email='', ra='', celular='', desconto=float, disciplinas=None):
        self.__nome = nome
        self.__email = email
        self.__ra = ra
        self.__celular = celular
        self.__desconto = desconto
     
    
        def retornaSobrenome(self):
        return ' '.join(self.__nome.split(' ')[1:])


    def retornaCargaHorario(self):
        carga_horaria = 0
        for d in self.__disciplinas:
            carga_horaria += d.getCargaHoraria()
        return carga_horaria * 6


# Create your models here.
