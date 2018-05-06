from django.db import models
from .pessoas import Pessoa

class Professor(Pessoa):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dtexpiracao = models.DateField(db_column='DtExpiracao')  # Field name made lowercase.
    apelido = models.CharField(db_column='Apelido', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Professor'
        app_label = 'disciplinas'

    def retornaCargaHoraria(self):
        soma_carga = 0
        