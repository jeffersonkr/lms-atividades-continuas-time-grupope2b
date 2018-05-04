from django.db import models
from .atividades import Atividade

class Atividadevinculada(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idatividade = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='IdAtividade')  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='IdProfessor')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='IdDisciplinaOfertada')  # Field name made lowercase.
    rotulo = models.CharField(db_column='Rotulo', max_length=20)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20)  # Field name made lowercase.
    dtiniciarespostas = models.DateField(db_column='DtIniciaRespostas')  # Field name made lowercase.
    dtfimresposta = models.DateField(db_column='DtfimResposta')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AtividadeVinculada'