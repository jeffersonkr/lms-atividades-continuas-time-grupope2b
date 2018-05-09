from django.db import models
from core.models.pessoas import Pessoa

class Coordenador(Pessoa):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dtexpiracao = models.DateField(db_column='DtExpiracao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Coordenador'
        app_label = 'disciplinas'