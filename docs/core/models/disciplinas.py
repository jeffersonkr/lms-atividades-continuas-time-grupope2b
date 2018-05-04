from django.db import models
from .coordenadores import Coordenador

class Disciplina(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', unique=True, max_length=30)  # Field name made lowercase.
    data = models.DateTimeField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=20)
    planodeensino = models.CharField(db_column='PlanoDeEnsino', max_length=300)  # Field name made lowercase.
    cargahoraria = models.IntegerField(db_column='CargaHoraria')  # Field name made lowercase.
    habilidades = models.CharField(db_column='Habilidades', max_length=30)  # Field name made lowercase.
    ementa = models.CharField(db_column='Ementa', max_length=30)  # Field name made lowercase.
    conteudoprogramatico = models.CharField(db_column='ConteudoProgramatico', max_length=30)  # Field name made lowercase.
    bibliografiabasica = models.CharField(db_column='BibliografiaBasica', max_length=100)  # Field name made lowercase.
    bibliografiacomplementar = models.CharField(db_column='BibliografiaComplementar', max_length=100)  # Field name made lowercase.
    percentualpratico = models.IntegerField(db_column='PercentualPratico')  # Field name made lowercase.
    percentualteorico = models.IntegerField(db_column='PercentualTeorico')  # Field name made lowercase.
    idcoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='IdCoordenador')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Disciplina'