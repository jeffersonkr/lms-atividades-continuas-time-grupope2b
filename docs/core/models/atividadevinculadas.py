from django.db import models
from .atividades import Atividade

class Atividadevinculada(models.Model):
    #id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    idatividade = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='IdAtividade')  # Field name made lowercase.
    idprofessor = models.ForeignKey('professores.Professor', models.DO_NOTHING, db_column='IdProfessor')  # Field name made lowercase.
    iddisciplinaOfertada = models.ForeignKey('DisciplinaOfertada', models.DO_NOTHING, db_column='IdDisciplinaOfertada')  # Field name made lowercase.
    rotulo = models.CharField(db_column='Rotulo', max_length=20)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20)  # Field name made lowercase.
    dtiniciarespostas = models.DateField(db_column='DtIniciaRespostas')  # Field name made lowercase.
    dtfimresposta = models.DateField(db_column='DtfimResposta')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'AtividadeVinculada'
        app_label = 'disciplinas'

    def __str__(self):
        return self.idatividade.titulo

    def atividadesNaoEnviadas(self):
        atividades = Atividadevinculada.objects.filter(iddisciplinaOfertada=self.id)
        atividadesAberto = []
        for atividade in atividades:
            if atividades.status == 'Aberta':
                atividadesAberto.append(atividade)

        return atividadesAberto

    def atividadesNaoEnviadas(self):
        atividades = Atividadevinculada.objects.filter(iddisciplinaOfertada=self.id)
        atividadesEncerrada = []
        for atividade in atividades:
            if atividades.status == 'Encerrada' or 'Fechada':
                atividadesAberto.append(atividade)

        return atividadesEncerrada

    