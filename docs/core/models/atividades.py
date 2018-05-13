from django.db import models


class Atividade(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    titulo = models.CharField(db_column='Titulo', unique=True, max_length=10)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=30, blank=True, null=True)  # Field name made lowercase.
    conteudo = models.CharField(db_column='Conteudo', max_length=50)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=15)  # Field name made lowercase.
    extras = models.CharField(db_column='Extras', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idprofessor = models.ForeignKey('professores.Professor', models.DO_NOTHING, db_column='IdProfessor')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Atividade'
        app_label = 'disciplinas'

    def __str__(self):
        return self.titulo
