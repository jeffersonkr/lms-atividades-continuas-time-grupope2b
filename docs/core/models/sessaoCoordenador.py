from core.models.coordenadores import Coordenador
from django.db import models
import uuid

class SessaoCoordenador(models.Model):

    id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)
    usuariocoordenador = models.ForeignKey(Coordenador, on_delete=models.CASCADE)
    

    class Meta:
        managed = True
        db_table = 'sessaoCoordenador'
        app_label = 'login'
