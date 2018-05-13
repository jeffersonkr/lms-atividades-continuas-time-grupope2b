from django.db import models
from .pessoas import Pessoa

class Professor(Pessoa):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dtexpiracao = models.DateField(db_column='DtExpiracao')  # Field name made lowercase.
    apelido = models.CharField(db_column='Apelido', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Professor'
        app_label = 'professores'

    def retornaCargaHoraria(self):
        soma_carga = 0
        from .disciplinas_ofertadas import DisciplinaOfertada
        disciplina = DisciplinaOfertada.objects.filter(idprofessor=self.id)
        for a in disciplina:
            b =  a.iddisciplina.cargahoraria
            soma_carga += b
        
        return soma_carga