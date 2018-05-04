from django.db import models

class Coordenador(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idlogin = models.CharField(unique=True, max_length=30)
    senha = models.CharField(max_length=15)
    nome = models.CharField(db_column='Nome', max_length=30)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=100)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', unique=True, max_length=14)  # Field name made lowercase.
    dtexpiracao = models.DateField(db_column='DtExpiracao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Coordenador'