create database ProjetoLMS
go

use ProjetoLMS
go


create table Coordenador (
	ID int NOT NULL identity(1,1)
	,idlogin varchar(30) not null
	,senha varchar(15) not null
	,Nome varchar(30) not null
	,Email varchar(100) not null
	,Celular varchar(14) not null
	, DtExpiracao date default ('19900101')
	,constraint PK_Coordenador
		primary key (ID)
	,constraint AK_login UNIQUE(idlogin)
	,constraint AK_Email unique(email)
	,constraint AK_Celular unique(celular)

);
go

create table Aluno (
	ID int not null identity(1,1)
	, idLogin varchar(30) not null
	, senha varchar(15) not null
	, Nome varchar(30) not null
	, email varchar(50) not null
	, celular varchar(14) not null
	, DtExpiracao date default ('19900101') not null
	, RA int not null
	, Foto varchar(50) not null
	, constraint PK_Aluno
		primary key (ID)
	,constraint AK_loginaluno UNIQUE(idlogin)
	,constraint AK_Emailaluno unique(email)
	,constraint AK_Celularaluno unique(celular)
);
GO


create table Professor (
	ID int not null identity(1,1)
	, idLogin varchar(30) not null
	, senha varchar(15) not null
	, Nome varchar(30) not null
	, email varchar(50) not null
	, celular varchar(14) not null
	, DtExpiracao  date default ('19900101') not null
	, Apelido varchar(20) not null
	, constraint PK_Professor
		primary key (ID)
	,constraint AK_loginprof UNIQUE(idlogin)
	,constraint AK_Emailprof unique(email)
	,constraint AK_Celularprof unique(celular)

);
go

create table Disciplina (
	ID int identity(1,1) not null
	, Nome varchar(30) not null
	, Data datetime default getdate()
	, status varchar(20) default ('Aberta') not null
	, PlanoDeEnsino varchar(300) not null
	, CargaHoraria int not null
	, Habilidades varchar(30) not null
	, Ementa varchar(30) not null
	, ConteudoProgramatico varchar(30) not null
	, BibliografiaBasica varchar(100) not null
	, BibliografiaComplementar varchar(100) not null
	, PercentualPratico int not null
	, PercentualTeorico int not null
	, IdCoordenador int not null
	, constraint PK_Disciplina
		primary key (ID)
	, constraint AK_Nome unique(Nome)
	, constraint CK_Status
		check (status in ('Aberta', 'Fechada'))
	, constraint CK_PercentPratico
		check (PercentualPratico >= 0 and PercentualPratico <= 100)
	, constraint CK_PercentTeorico
		check (PercentualTeorico >= 0 and PercentualTeorico <= 100)
	, constraint FK_IdCoordenador
		foreign key (IdCoordenador)
		references Coordenador(ID)

);
go


create table Curso (
	ID int identity(1,1) not null
	, nome varchar(20)
	, constraint PK_Curso
		primary key (ID)
	, constraint AK_NomeCurso unique(nome)
)
go


create table DisciplinaOfertada (
	ID int identity(1,1) not null
	, IdCoordenador int not null
	, DtinicioMatricula date
	, DtFimMatricula date
	, IdDisciplina int not null
	, IdCurso int not null
	, Ano int not null
	, Semestre int not null
	, Turma varchar(1) not null
	, IdProfessor int
	, Metodologia varchar(100)
	, Recursos varchar(100)
	, CriterioAvaliacao varchar(100)
	, PlanoDeAulas varchar(100)
	, constraint PK_DisciplinaOfertada
		primary key (ID)
	, constraint FK_IdDisciplina
		foreign key (IdDisciplina)
		references Disciplina(ID)
	, constraint FK_IdCurso
		foreign key (IdCurso)
		references Curso(ID)
	, constraint CK_Ano
		check (Ano>=1900 and Ano <=2100)
	, constraint CK_Semestre
		check (Semestre >=1 and Semestre <= 2)
	, constraint CK_Turma
		check (Turma not like '%[^A-Z]%')
	, constraint FK_IdProfessor
		foreign key (IdProfessor)
		references Professor(ID)
);
go


create table SolicitacaoMatricula(
	ID int identity(1,1) not null
	, IdAluno int not null
	, IdDisciplinaOfer int not null
	, DtSolicitacao datetime default getdate()
	, IdCoordenador int
	, status varchar(10) default('Solicitada')
	, constraint PK_SolicitacaoMAT
		primary key (ID)
	, constraint FK_IdAluno
		foreign key (IdAluno)
		references Aluno(ID)
	, constraint FK_IdDisciplinaOfertada
		foreign key (IdDisciplinaOfer)
		references DisciplinaOfertada(ID)
	, constraint CK_statusSolMatri
		check (status in ('Solicitada', 'Aprovada', 'Rejeitada', 'Cancelada'))
	
);
go

create table Atividade(
	ID int identity(1,1) not null
	, Titulo varchar(10) not null
	, Descricao varchar(30)
	, Conteudo varchar(50) not null
	, Tipo varchar(15) not null
	, Extras varchar(20)
	, IdProfessor int not null
	, constraint PK_Atividade
		primary key (ID)
	, constraint AK_titulo unique(Titulo)
	, constraint CK_Tipo
		check (Tipo in ('Resposta Aberta', 'Teste'))
	, constraint FK_Atividade
		foreign key (IdProfessor)
		references Professor(ID)
);
go

create table AtividadeVinculada(
	ID int identity(1,1) not null
	, IdAtividade int not null
	, IdProfessor int not null
	, IdDisciplinaOfertada int not null
	, Rotulo varchar(20) not null
	, Status varchar(20) not null
	, DtIniciaRespostas date not null
	, DtfimResposta date not null
	, constraint PK_AtividadeVinculada
		primary key (ID)
	, constraint FK_AtividadeVinculada
		foreign key (IdAtividade)
		references Atividade(ID)
	, constraint FK_AtividadeVinculadaProf
		foreign key (IdProfessor)
		references Professor(ID)
	, constraint FK_AtividadeVinculadaOfertada
		foreign key (IdDisciplinaOfertada)
		references DisciplinaOfertada(ID)
	, constraint CK_StatusAtividade
		check (Status in ('Disponibilizada', 'Aberta', 'Fechada', 'Encerrada', 'Prorrogada'))

);
go

/*Criação da tabela de entrega */

create table Entrega(
	ID int identity(1,1) not null
	,IdAluno int not null
	,IdAtividadeVinculada int not null
	,Titulo varchar(10) not null
	,Resposta varchar(50) not null
	,DtEntrega date default getdate()
	,Status varchar(20) default ('Entregue')
	,IdProfessor int
	,Nota int
	,DtAvaliacao date
	,Obs varchar(30)
	, constraint PK_Entrega
		primary key (ID)
	, constraint FK_EntregaAluno
		foreign key (IdAluno)
		references Aluno(ID)
	, constraint FK_EntradaAtVinculada
		foreign key (IdAtividadeVinculada)
		references AtividadeVinculada(ID)
	, constraint CK_StatusEntrega
		check (Status in ('Entregue', 'Corrigido'))
	, constraint FK_EntregaIdProfessor
		foreign key (IdProfessor)
		references Professor(ID)
	, constraint CK_Nota
		check (Nota >= 0.00 and Nota <= 10.00)
);
go


/* Criação da table de Mensagem */

create table Mensagem(
	ID int identity(1,1) not null
	, IdAluno int not null
	, IdProfessor int not null
	, Assunto varchar(20) not null
	, Referencia varchar(20) not null
	, Conteudo varchar(500) not null
	, Status varchar(20) default ('')
	, DtEnvio date default getdate() not null
	, DtResposta date
	, Resposta varchar(500)
	, constraint PK_Mensagem
		primary key (ID)
	, constraint FK_MensagemAluno
		foreign key (IdAluno)
		references Aluno(ID)
	, constraint FK_MensagemProfessor
		foreign key (IdProfessor)
		references Professor(ID)
	, constraint AK_StatusMsg unique(Status)

);
go

/*População do banco de dados Coordenador, Alunos e Professores */

INSERT INTO Coordenador(idlogin,senha,Nome,Email,Celular,DtExpiracao)
VALUES ('1','abc','Gustavo','gustavo@impacta.com.br','11959906668','')
go

INSERT INTO  Aluno(idLogin,senha,Nome,email,celular,DtExpiracao,RA,Foto)
VALUES ('1','abc123','Marcio','marcio.xisde@gmail.com','11959906668','','1701580','')
go

INSERT INTO  Aluno(idLogin,senha,Nome,email,celular,DtExpiracao,RA,Foto)
VALUES ('2','abc456','Felipe','felipe_futedol@hotmail.com','11123658984','','1702680','')
go

INSERT INTO  Aluno(idLogin,senha,Nome,email,celular,DtExpiracao,RA,Foto)
VALUES ('3','456efh','Clovis','clovis.futedol@hotmail.com','1127456325','','1805680','')
go

INSERT INTO  Aluno(idLogin,senha,Nome,email,celular,DtExpiracao,RA,Foto) 
VALUES ('4','efg456','Maria','maria.zica@hotmail.com','1165365478','','1812280','')
go

INSERT INTO  Aluno(idLogin,senha,Nome,email,celular,DtExpiracao,RA,Foto)
VALUES ('5','ked789','Joana','joana@gmail.com','1125963584','','1701480','')
go

INSERT INTO  Aluno(idLogin,senha,Nome,email,celular,DtExpiracao,RA,Foto) 
VALUES ('6','alp973','Esther','teka@gmail.com','11956325558','','1701480','')
go

INSERT INTO  Aluno(idLogin,senha,Nome,email,celular,DtExpiracao,RA,Foto) 
VALUES ('7','165DDFG','Lucas','lucas17@gmail.com','116523856','','1749380','')
go

INSERT INTO  Aluno(idLogin,senha,Nome,email,celular,DtExpiracao,RA,Foto) 
VALUES ('8','54DCDS','Miguel','daguerra@gmail.com','1125635963','','1703658','')
go

INSERT INTO  Aluno(idLogin,senha,Nome,email,celular,DtExpiracao,RA,Foto) 
VALUES ('9','aa236','Victor','victor133@gmail.com','1125635698','','1703658','')
go

INSERT INTO  Aluno(idLogin,senha,Nome,email,celular,DtExpiracao,RA,Foto) 
VALUES ('10','63dfd','Guerra','Gu156@gmail.com','1125963548','','1703562','')
go

INSERT INTO Professor (idLogin,senha,Nome,email,celular,DtExpiracao,Apelido) 
VALUES ('1','minha','Rafael Almeida', 'rafael15@gmail.com','11959906668','13-05-2020','rafa')
go

INSERT INTO Professor (idLogin,senha,Nome,email,celular,DtExpiracao,Apelido) 
VALUES ('2','lala12','Clovis', 'clovisbr@gmail.com','11563256668','07-03-2020','kid')
go

INSERT INTO Professor (idLogin,senha,Nome,email,celular,DtExpiracao,Apelido) 
VALUES ('3','senhaa15','Miguel', 'miguelg@gmail.com','1123658963','13-08-2022','Guel')
go

INSERT INTO Professor (idLogin,senha,Nome,email,celular,DtExpiracao,Apelido) 
VALUES ('4','a123a45','Jurema', 'jurema18@gmail.com','1125486325','22-02-2025','Ju')
go

INSERT INTO Professor (idLogin,senha,Nome,email,celular,DtExpiracao,Apelido) 
VALUES ('5','ghkk','Maria', 'marizinha@gmail.com','11923563325','10-06-2030','marizinha')
go

/*Criação de todos os cursos da faculdade*/

INSERT INTO CURSO (nome) VALUES ('ADS')
go

INSERT INTO CURSO (nome) VALUES ('SI')
go

INSERT INTO CURSO (nome) VALUES ('ADM')
go

INSERT INTO CURSO (nome) VALUES ('BD')
go

INSERT INTO CURSO (nome) VALUES ('PG')
go

INSERT INTO CURSO (nome) VALUES ('GTI')
go

/* Criação de Disciplinas no plano de ensino */


INSERT INTO Disciplina (Nome, PlanoDeEnsino, CargaHoraria, Habilidades, Ementa ,ConteudoProgramatico, BibliografiaBasica, BibliografiaComplementar, PercentualPratico, PercentualTeorico, IdCoordenador)
VALUES ('Linguagem SQL', 'Plano de Ensino', 80, 'Desenvolvimento Base de Dados','Criando um banco de dados' ,'Modelagem Relacional', 'Gerenciando Banco de Dados - A Abordagem Entidade-Relacionamento para Projeto Lógico', 'CHEN, P. Gerenciando Banco de Dados -
Editora MCGraw-Hill, 1990.', 70, 30, 1)
go

INSERT INTO Disciplina (Nome, PlanoDeEnsino, CargaHoraria, Habilidades, Ementa ,ConteudoProgramatico, BibliografiaBasica, BibliografiaComplementar, PercentualPratico, PercentualTeorico, IdCoordenador)
VALUES ('Tec Web', 'Plano de Ensino', 80, 'Desenvolvimento sustentaveis','Conceito de DevOps' ,'Agile Lean Integração contínua', 'Continuous Delivery: Reliable Software Releases through Build, Test, and Deployment Automation',
'HUMBLE, J. Pearson Education, 2010', 50, 50, 1 )
go

/*Ofertar disciplina de Linguagem SQL*/

INSERT INTO DisciplinaOfertada (IdCoordenador, DtinicioMatricula, DtFimMatricula, IdDisciplina, IdCurso, Ano, Semestre, Turma, IdProfessor)
VALUES (1, '01/01/2017', '01/06/2017', 1, 4, 2017, 1, 'A', 1 )
go

/* Alterando o pofessor de uma disciplina já ofertada */
UPDATE DisciplinaOfertada 
SET IdProfessor = 2
WHERE IdProfessor = 1 
go

UPDATE DisciplinaOfertada 
SET Metodologia  = 'Banco', Recursos = 'Nenhum', CriterioAvaliacao = 'Notas', PlanoDeAulas = 'Segunda-feira'
WHERE ID = 2 
go

/* Alteração de data inicio e fim da matricula da disciplina ofertada */

UPDATE DisciplinaOfertada
SET DtinicioMatricula =  '01/06/2017', DtFimMatricula = '01/01/2018'
WHERE ID = 2 
go

/* Inserindo solicitação de matrícula de 3 alunos */

INSERT INTO SolicitacaoMatricula (IdAluno, IdDisciplinaOfer, IdCoordenador)
VALUES (1, 1, 1)
go

INSERT INTO SolicitacaoMatricula (IdAluno, IdDisciplinaOfer, IdCoordenador)
VALUES (2, 1, 1)
go

INSERT INTO SolicitacaoMatricula (IdAluno, IdDisciplinaOfer, IdCoordenador)
VALUES (3, 1, 1)
go


/*Alterando a situação de Solicitação de Matricula */
UPDATE SolicitacaoMatricula
SET status = 'Aprovada'
WHERE ID = 1
go

UPDATE SolicitacaoMatricula
SET status = 'Rejeitada'
where ID = 2
go

UPDATE SolicitacaoMatricula
SET status = 'Cancelada'
where ID = 3
go


/*Inserindo Atividades*/
INSERT into Atividade (Titulo, Descricao, Conteudo, Tipo, IdProfessor)
VALUES ('AC6', 'Descricao pendente!!', 'INSERT,UPDATE,DELETE', 'Teste', 1)
go

INSERT into Atividade (Titulo, Descricao, Conteudo, Tipo, IdProfessor)
VALUES ('AC7', 'Descricao secreta!!', 'CREATE TABLE', 'Teste', 2)
go


/*Vincular Atividade ao SQL*/
sp_help AtividadeVinculada
INSERT into AtividadeVinculada (IdAtividade, IdProfessor, IdDisciplinaOfertada, Rotulo, Status, DtIniciaRespostas, DtfimResposta)
VALUES (2, 2, 1, 'ATIVIDADE', 'Prorrogada', '2018-04-16', '2018-04-17')
go

/*Entregas de Atividades*/
sp_help Entrega
select * from Entrega

INSERT into Entrega(IdAluno, IdAtividadeVinculada, Titulo, Resposta)
VALUES (1, 1, 'Atividade', 'Resposta 100% correta')
go

INSERT into Entrega(IdAluno, IdAtividadeVinculada, Titulo, Resposta)
VALUES (2, 1, 'AC7', 'Resposta 100% errada')
go


/*Atualizando a entrega*/

UPDATE Entrega
SET IdProfessor = 2 , Nota = 10.00
WHERE Titulo = 'Atividade'

/*Mensagem para o Professor*/
sp_help mensagem

INSERT into Mensagem(IdAluno,IdProfessor, Assunto,Referencia,Conteudo)
VALUES (2, 2, 'Entrega Atividade', 'SQL', 'Qual a data de entrega da AC6?')
go

UPDATE Mensagem
set Resposta = 'Para a proxima semana', Status = 'Respondida', DtResposta = '2018-04-16'
where ID = 1