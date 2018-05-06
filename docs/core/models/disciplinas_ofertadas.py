from django.db import models
from .disciplinas import Disciplina
from .cursos import Curso

class DisciplinaOfertada(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idcoordenador = models.IntegerField(db_column='IdCoordenador')  # Field name made lowercase.
    dtiniciomatricula = models.DateField(db_column='DtinicioMatricula', blank=True, null=True)  # Field name made lowercase.
    dtfimmatricula = models.DateField(db_column='DtFimMatricula', blank=True, null=True)  # Field name made lowercase.
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.
    idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='IdCurso')  # Field name made lowercase.
    ano = models.IntegerField(db_column='Ano')  # Field name made lowercase.
    semestre = models.IntegerField(db_column='Semestre')  # Field name made lowercase.
    turma = models.CharField(db_column='Turma', max_length=1)  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='IdProfessor', blank=True, null=True)  # Field name made lowercase.
    metodologia = models.CharField(db_column='Metodologia', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recursos = models.CharField(db_column='Recursos', max_length=100, blank=True, null=True)  # Field name made lowercase.
    criterioavaliacao = models.CharField(db_column='CriterioAvaliacao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    planodeaulas = models.CharField(db_column='PlanoDeAulas', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'DisciplinaOfertada'
        app_label = 'disciplinas'