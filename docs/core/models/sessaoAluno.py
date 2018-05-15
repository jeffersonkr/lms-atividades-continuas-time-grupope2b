from core.models.alunos import Aluno
from django.db import models
import uuid

class SessaoAluno(models.Model):

    id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    usuarioaluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    

    class Meta:
        managed = True
        db_table = 'sessaoAluno'
        app_label = 'login'
