from core.models.alunos import Aluno
from core.models.professores import Professor
from core.models.coordenadores import Coordenador


class Sessao(models.Model):

    id = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False)

    usuario = models.ForeignKey(Professor or Aluno or Coordenador, on_delete=models.CASCADE)