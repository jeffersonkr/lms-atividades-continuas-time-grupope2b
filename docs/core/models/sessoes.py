from core.models.alunos import Aluno
from core.models.professores import Professor
from core.models.coordenadores import Coordenador
from django.db import models
import uuid
from django.core.exceptions import ObjectDoesNotExist

class Sessao(models.Model):

    id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    usuarioaluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    usuarioprofessor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    usuariocoordenador = models.ForeignKey(Coordenador, on_delete=models.CASCADE)


    class Meta:
        managed = True
        db_table = 'Sessao'
        app_label = 'login'