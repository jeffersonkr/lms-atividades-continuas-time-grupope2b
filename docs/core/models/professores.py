from django.db import models

class Professor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idlogin = models.CharField(db_column='idLogin', unique=True, max_length=30)  # Field name made lowercase.
    senha = models.CharField(max_length=15)
    nome = models.CharField(db_column='Nome', max_length=30)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=50)
    celular = models.CharField(unique=True, max_length=14)
    dtexpiracao = models.DateField(db_column='DtExpiracao')  # Field name made lowercase.
    apelido = models.CharField(db_column='Apelido', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Professor'