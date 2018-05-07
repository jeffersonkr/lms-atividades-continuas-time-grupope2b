from django.db import models
from .alunos import Aluno
from .atividadevinculadas import Atividadevinculada

class Entrega(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='IdAluno')  # Field name made lowercase.
    idatividadevinculada = models.ForeignKey(Atividadevinculada, models.DO_NOTHING, db_column='IdAtividadeVinculada')  # Field name made lowercase.
    titulo = models.CharField(db_column='Titulo', max_length=10)  # Field name made lowercase.
    resposta = models.CharField(db_column='Resposta', max_length=50)  # Field name made lowercase.
    dtentrega = models.DateField(db_column='DtEntrega', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='IdProfessor', blank=True, null=True)  # Field name made lowercase.
    nota = models.IntegerField(db_column='Nota', blank=True, null=True)  # Field name made lowercase.
    dtavaliacao = models.DateField(db_column='DtAvaliacao', blank=True, null=True)  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Entrega'
        
        app_label = 'disciplinas'

    def __str__(self):
        return self.titulo

    def alunosComNota(self):
        alunos=[]
        from .atividadevinculadas import Atividadevinculada
        atividades = Atividadevinculada.objects.get(id=self.idatividadevinculada)
        for atividadeNota in atividades:
            if atividadeNota != None:
                alunos += atividadeNota.idaluno
        return alunos

    def alunosSemNota(self):
        alunos=[]
        atividades = Atividadevinculada.objects.filter(id=self.idatividadevinculada)
        for atividadeNota in atividades:
            if atividadeNota is None:
                alunos += atividadeNota.idaluno
        return alunos
    