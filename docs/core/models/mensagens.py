from django.db import models
from .alunos import Aluno

class Mensagem(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='IdAluno')  # Field name made lowercase.
    idprofessor = models.ForeignKey('professores.Professor', models.DO_NOTHING, db_column='IdProfessor')  # Field name made lowercase.
    assunto = models.CharField(db_column='Assunto', max_length=20)  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=20)  # Field name made lowercase.
    conteudo = models.CharField(db_column='Conteudo', max_length=500)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dtenvio = models.DateField(db_column='DtEnvio')  # Field name made lowercase.
    dtresposta = models.DateField(db_column='DtResposta', blank=True, null=True)  # Field name made lowercase.
    resposta = models.CharField(db_column='Resposta', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Mensagem'
        app_label = 'disciplinas'

    def __str__(self):
        return self.assunto

    