from django.db import models
from .pessoas import Pessoa

class Aluno(Pessoa):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dtexpiracao = models.DateField(db_column='DtExpiracao')  # Field name made lowercase.
    ra = models.IntegerField(db_column='RA')  # Field name made lowercase.
    foto = models.CharField(db_column='Foto', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Aluno'
        app_label = 'disciplinas'

    def retornaCargaHoraria(self):
        soma_carga = 0
        from .solicitacao_matriculas import SolicitacaoMatricula

        solicitacoes = SolicitacaoMatricula.objects.filter(idaluno=self.id)

        for s in solicitacoes:
            soma_carga += s.iddisciplinaofer.iddisciplina.cargahoraria

        return soma_carga
    
    