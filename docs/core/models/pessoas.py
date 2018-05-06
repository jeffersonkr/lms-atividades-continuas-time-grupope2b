from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(db_column='Nome', max_length=30)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=50)
    celular = models.CharField(unique=True, max_length=14)
    idlogin = models.CharField(db_column='idLogin', unique=True, max_length=30)  # Field name made lowercase.
    senha = models.CharField(max_length=15)
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.nome

    def retornaSobrenome(self):
        return ' '.join(self.nome.split(' ')[1:])
        
    def retornaCargaHoraria(self):
        return 'Método não implementado'
