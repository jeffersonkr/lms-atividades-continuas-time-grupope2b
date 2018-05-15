from core.models.professores import Professor
from django.db import models
import uuid

class SessaoProfessor(models.Model):

    id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    usuarioprofessor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    

    class Meta:
        managed = True
        db_table = 'sessaoProfessor'
        app_label = 'login'
