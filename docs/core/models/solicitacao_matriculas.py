from django.db import models
from .alunos import Aluno
from .disciplinas_ofertadas import DisciplinaOfertada

class SolicitacaoMatricula(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='IdAluno')  # Field name made lowercase.
    iddisciplinaofer = models.ForeignKey(DisciplinaOfertada, models.DO_NOTHING, db_column='IdDisciplinaOfer')  # Field name made lowercase.
    dtsolicitacao = models.DateTimeField(db_column='DtSolicitacao', blank=True, null=True)  # Field name made lowercase.
    idcoordenador = models.IntegerField(db_column='IdCoordenador', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'SolicitacaoMatricula'
        app_label = 'disciplinas'