# Generated by Django 2.0.4 on 2018-05-04 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('idlogin', models.CharField(db_column='idLogin', max_length=30, unique=True)),
                ('senha', models.CharField(max_length=15)),
                ('nome', models.CharField(db_column='Nome', max_length=30)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('celular', models.CharField(max_length=14, unique=True)),
                ('dtexpiracao', models.DateField(db_column='DtExpiracao')),
                ('ra', models.IntegerField(db_column='RA')),
                ('foto', models.CharField(db_column='Foto', max_length=50)),
            ],
            options={
                'db_table': 'Aluno',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('titulo', models.CharField(db_column='Titulo', max_length=10, unique=True)),
                ('descricao', models.CharField(blank=True, db_column='Descricao', max_length=30, null=True)),
                ('conteudo', models.CharField(db_column='Conteudo', max_length=50)),
                ('tipo', models.CharField(db_column='Tipo', max_length=15)),
                ('extras', models.CharField(blank=True, db_column='Extras', max_length=20, null=True)),
            ],
            options={
                'db_table': 'Atividade',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Atividadevinculada',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('rotulo', models.CharField(db_column='Rotulo', max_length=20)),
                ('status', models.CharField(db_column='Status', max_length=20)),
                ('dtiniciarespostas', models.DateField(db_column='DtIniciaRespostas')),
                ('dtfimresposta', models.DateField(db_column='DtfimResposta')),
            ],
            options={
                'db_table': 'AtividadeVinculada',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('idlogin', models.CharField(max_length=30, unique=True)),
                ('senha', models.CharField(max_length=15)),
                ('nome', models.CharField(db_column='Nome', max_length=30)),
                ('email', models.CharField(db_column='Email', max_length=100, unique=True)),
                ('celular', models.CharField(db_column='Celular', max_length=14, unique=True)),
                ('dtexpiracao', models.DateField(blank=True, db_column='DtExpiracao', null=True)),
            ],
            options={
                'db_table': 'Coordenador',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('sigla', models.CharField(max_length=3)),
            ],
            options={
                'db_table': 'Curso',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(db_column='Nome', max_length=30, unique=True)),
                ('data', models.DateTimeField(blank=True, db_column='Data', null=True)),
                ('status', models.CharField(max_length=20)),
                ('planodeensino', models.CharField(db_column='PlanoDeEnsino', max_length=300)),
                ('cargahoraria', models.IntegerField(db_column='CargaHoraria')),
                ('habilidades', models.CharField(db_column='Habilidades', max_length=30)),
                ('ementa', models.CharField(db_column='Ementa', max_length=30)),
                ('conteudoprogramatico', models.CharField(db_column='ConteudoProgramatico', max_length=30)),
                ('bibliografiabasica', models.CharField(db_column='BibliografiaBasica', max_length=100)),
                ('bibliografiacomplementar', models.CharField(db_column='BibliografiaComplementar', max_length=100)),
                ('percentualpratico', models.IntegerField(db_column='PercentualPratico')),
                ('percentualteorico', models.IntegerField(db_column='PercentualTeorico')),
            ],
            options={
                'db_table': 'Disciplina',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Disciplinaofertada',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('idcoordenador', models.IntegerField(db_column='IdCoordenador')),
                ('dtiniciomatricula', models.DateField(blank=True, db_column='DtinicioMatricula', null=True)),
                ('dtfimmatricula', models.DateField(blank=True, db_column='DtFimMatricula', null=True)),
                ('ano', models.IntegerField(db_column='Ano')),
                ('semestre', models.IntegerField(db_column='Semestre')),
                ('turma', models.CharField(db_column='Turma', max_length=1)),
                ('metodologia', models.CharField(blank=True, db_column='Metodologia', max_length=100, null=True)),
                ('recursos', models.CharField(blank=True, db_column='Recursos', max_length=100, null=True)),
                ('criterioavaliacao', models.CharField(blank=True, db_column='CriterioAvaliacao', max_length=100, null=True)),
                ('planodeaulas', models.CharField(blank=True, db_column='PlanoDeAulas', max_length=100, null=True)),
            ],
            options={
                'db_table': 'DisciplinaOfertada',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Entrega',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('titulo', models.CharField(db_column='Titulo', max_length=10)),
                ('resposta', models.CharField(db_column='Resposta', max_length=50)),
                ('dtentrega', models.DateField(blank=True, db_column='DtEntrega', null=True)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=20, null=True)),
                ('nota', models.IntegerField(blank=True, db_column='Nota', null=True)),
                ('dtavaliacao', models.DateField(blank=True, db_column='DtAvaliacao', null=True)),
                ('obs', models.CharField(blank=True, db_column='Obs', max_length=30, null=True)),
            ],
            options={
                'db_table': 'Entrega',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('assunto', models.CharField(db_column='Assunto', max_length=20)),
                ('referencia', models.CharField(db_column='Referencia', max_length=20)),
                ('conteudo', models.CharField(db_column='Conteudo', max_length=500)),
                ('status', models.CharField(blank=True, db_column='Status', max_length=20, null=True, unique=True)),
                ('dtenvio', models.DateField(db_column='DtEnvio')),
                ('dtresposta', models.DateField(blank=True, db_column='DtResposta', null=True)),
                ('resposta', models.CharField(blank=True, db_column='Resposta', max_length=500, null=True)),
            ],
            options={
                'db_table': 'Mensagem',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('idlogin', models.CharField(db_column='idLogin', max_length=30, unique=True)),
                ('senha', models.CharField(max_length=15)),
                ('nome', models.CharField(db_column='Nome', max_length=30)),
                ('email', models.CharField(max_length=50, unique=True)),
                ('celular', models.CharField(max_length=14, unique=True)),
                ('dtexpiracao', models.DateField(db_column='DtExpiracao')),
                ('apelido', models.CharField(db_column='Apelido', max_length=20)),
            ],
            options={
                'db_table': 'Professor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Solicitacaomatricula',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('dtsolicitacao', models.DateTimeField(blank=True, db_column='DtSolicitacao', null=True)),
                ('idcoordenador', models.IntegerField(blank=True, db_column='IdCoordenador', null=True)),
                ('status', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'SolicitacaoMatricula',
                'managed': False,
            },
        ),
    ]