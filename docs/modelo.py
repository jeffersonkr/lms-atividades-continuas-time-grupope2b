# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Aluno(models.Model):
    nome = models.CharField(db_column='Nome', max_length=30)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=50)
    celular = models.CharField(unique=True, max_length=14)
    idlogin = models.CharField(db_column='idLogin', unique=True, max_length=30)  # Field name made lowercase.
    senha = models.CharField(max_length=15)
    dtexpiracao = models.DateField(db_column='DtExpiracao')  # Field name made lowercase.
    ra = models.IntegerField(db_column='RA')  # Field name made lowercase.
    foto = models.CharField(db_column='Foto', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Aluno'


class Atividade(models.Model):
    titulo = models.CharField(db_column='Titulo', unique=True, max_length=10)  # Field name made lowercase.
    descricao = models.CharField(db_column='Descricao', max_length=30, blank=True, null=True)  # Field name made lowercase.
    conteudo = models.CharField(db_column='Conteudo', max_length=50)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=15)  # Field name made lowercase.
    extras = models.CharField(db_column='Extras', max_length=20, blank=True, null=True)  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='IdProfessor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Atividade'


class Atividadevinculada(models.Model):
    rotulo = models.CharField(db_column='Rotulo', max_length=20)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20)  # Field name made lowercase.
    dtiniciarespostas = models.DateField(db_column='DtIniciaRespostas')  # Field name made lowercase.
    dtfimresposta = models.DateField(db_column='DtfimResposta')  # Field name made lowercase.
    idatividade = models.ForeignKey(Atividade, models.DO_NOTHING, db_column='IdAtividade')  # Field name made lowercase.
    iddisciplinaofertada = models.ForeignKey('Disciplinaofertada', models.DO_NOTHING, db_column='IdDisciplinaOfertada')  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='IdProfessor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AtividadeVinculada'


class Coordenador(models.Model):
    nome = models.CharField(db_column='Nome', max_length=30)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=50)
    celular = models.CharField(unique=True, max_length=14)
    idlogin = models.CharField(db_column='idLogin', unique=True, max_length=30)  # Field name made lowercase.
    senha = models.CharField(max_length=15)
    dtexpiracao = models.DateField(db_column='DtExpiracao', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Coordenador'


class Curso(models.Model):
    nome = models.CharField(unique=True, max_length=50)
    sigla = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'Curso'


class Disciplina(models.Model):
    nome = models.CharField(db_column='Nome', unique=True, max_length=30)  # Field name made lowercase.
    data = models.DateTimeField(db_column='Data', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=20)
    planodeensino = models.CharField(db_column='PlanoDeEnsino', max_length=300)  # Field name made lowercase.
    cargahoraria = models.IntegerField(db_column='CargaHoraria')  # Field name made lowercase.
    habilidades = models.CharField(db_column='Habilidades', max_length=30)  # Field name made lowercase.
    ementa = models.CharField(db_column='Ementa', max_length=30)  # Field name made lowercase.
    conteudoprogramatico = models.CharField(db_column='ConteudoProgramatico', max_length=30)  # Field name made lowercase.
    bibliografiabasica = models.CharField(db_column='BibliografiaBasica', max_length=100)  # Field name made lowercase.
    bibliografiacomplementar = models.CharField(db_column='BibliografiaComplementar', max_length=100)  # Field name made lowercase.
    percentualpratico = models.IntegerField(db_column='PercentualPratico')  # Field name made lowercase.
    percentualteorico = models.IntegerField(db_column='PercentualTeorico')  # Field name made lowercase.
    idcoordenador = models.ForeignKey(Coordenador, models.DO_NOTHING, db_column='IdCoordenador')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Disciplina'


class Disciplinaofertada(models.Model):
    idcoordenador = models.IntegerField(db_column='IdCoordenador')  # Field name made lowercase.
    dtiniciomatricula = models.DateField(db_column='DtinicioMatricula', blank=True, null=True)  # Field name made lowercase.
    dtfimmatricula = models.DateField(db_column='DtFimMatricula', blank=True, null=True)  # Field name made lowercase.
    ano = models.IntegerField(db_column='Ano')  # Field name made lowercase.
    semestre = models.IntegerField(db_column='Semestre')  # Field name made lowercase.
    turma = models.CharField(db_column='Turma', max_length=1)  # Field name made lowercase.
    metodologia = models.CharField(db_column='Metodologia', max_length=100, blank=True, null=True)  # Field name made lowercase.
    recursos = models.CharField(db_column='Recursos', max_length=100, blank=True, null=True)  # Field name made lowercase.
    criterioavaliacao = models.CharField(db_column='CriterioAvaliacao', max_length=100, blank=True, null=True)  # Field name made lowercase.
    planodeaulas = models.CharField(db_column='PlanoDeAulas', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idcurso = models.ForeignKey(Curso, models.DO_NOTHING, db_column='IdCurso')  # Field name made lowercase.
    iddisciplina = models.ForeignKey(Disciplina, models.DO_NOTHING, db_column='IdDisciplina')  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='IdProfessor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DisciplinaOfertada'


class Entrega(models.Model):
    titulo = models.CharField(db_column='Titulo', max_length=10)  # Field name made lowercase.
    resposta = models.CharField(db_column='Resposta', max_length=50)  # Field name made lowercase.
    dtentrega = models.DateField(db_column='DtEntrega', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nota = models.IntegerField(db_column='Nota', blank=True, null=True)  # Field name made lowercase.
    dtavaliacao = models.DateField(db_column='DtAvaliacao', blank=True, null=True)  # Field name made lowercase.
    obs = models.CharField(db_column='Obs', max_length=30, blank=True, null=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='IdAluno')  # Field name made lowercase.
    idatividadevinculada = models.ForeignKey(Atividadevinculada, models.DO_NOTHING, db_column='IdAtividadeVinculada')  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='IdProfessor', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Entrega'


class Mensagem(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    assunto = models.CharField(db_column='Assunto', max_length=20)  # Field name made lowercase.
    referencia = models.CharField(db_column='Referencia', max_length=20)  # Field name made lowercase.
    conteudo = models.CharField(db_column='Conteudo', max_length=500)  # Field name made lowercase.
    status = models.CharField(db_column='Status', unique=True, max_length=20, blank=True, null=True)  # Field name made lowercase.
    dtenvio = models.DateField(db_column='DtEnvio')  # Field name made lowercase.
    dtresposta = models.DateField(db_column='DtResposta', blank=True, null=True)  # Field name made lowercase.
    resposta = models.CharField(db_column='Resposta', max_length=500, blank=True, null=True)  # Field name made lowercase.
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='IdAluno')  # Field name made lowercase.
    idprofessor = models.ForeignKey('Professor', models.DO_NOTHING, db_column='IdProfessor')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Mensagem'


class Professor(models.Model):
    nome = models.CharField(db_column='Nome', max_length=30)  # Field name made lowercase.
    email = models.CharField(unique=True, max_length=50)
    celular = models.CharField(unique=True, max_length=14)
    idlogin = models.CharField(db_column='idLogin', unique=True, max_length=30)  # Field name made lowercase.
    senha = models.CharField(max_length=15)
    dtexpiracao = models.DateField(db_column='DtExpiracao')  # Field name made lowercase.
    apelido = models.CharField(db_column='Apelido', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Professor'


class Solicitacaomatricula(models.Model):
    dtsolicitacao = models.DateTimeField(db_column='DtSolicitacao', blank=True, null=True)  # Field name made lowercase.
    idcoordenador = models.IntegerField(db_column='IdCoordenador', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(max_length=10, blank=True, null=True)
    idaluno = models.ForeignKey(Aluno, models.DO_NOTHING, db_column='IdAluno')  # Field name made lowercase.
    iddisciplinaofer = models.ForeignKey(Disciplinaofertada, models.DO_NOTHING, db_column='IdDisciplinaOfer')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SolicitacaoMatricula'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Sessoes(models.Model):
    id = models.CharField(primary_key=True, max_length=32)
    usuario = models.ForeignKey(Professor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sessoes'
