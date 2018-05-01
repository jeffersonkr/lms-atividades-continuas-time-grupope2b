from django.db import models

class Cursos(models.Model):
    #id = models.IntegerField(blank=True, null=True)
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=3)

    def __str__(self):
        return self.sigla

    class Meta:
        managed = False
        db_table = 'Cursos'

class Disciplina(models.Model):
   
    nome = models.CharField(unique=True, max_length=255)
    nomecurso = models.CharField(db_column='nomeCurso', unique=True, max_length=30)  # Field name made lowercase.
    curso = models.ForeignKey(Cursos, models.DO_NOTHING, db_column='id_curso')

    class Meta:
        managed = False
        db_table = 'Disciplina'