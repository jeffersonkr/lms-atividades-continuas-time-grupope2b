class Aluno:
    
    def __init__(self, nome='', email='', ra='', celular='', desconto=float, disciplinas=None):
        self.__nome = nome
        self.__email = email
        self.__ra = ra
        self.__celular = celular
        self.__desconto = desconto
        self.__disciplinas = []

    def getNome(self):
        return self.__nome
    def setNome(self, nome):
        self.__nome = nome

    def getEmail(self):
        return self.__email
    def setEmail(self, email):
        self.__email = email

    def getRa(self):
        return self.__ra
    
    def getCelular(self):
        return self.__celular
    def setCelular(self, celular):
        self.__celular = celular

    def getDesconto(self):
        return self.__desconto
    def setDesconto(self, desconto):
        self.__desconto = desconto
    
    def getDisciplinas(self):
        return self.__disciplinas

    def adicionaDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)

    
    def aumentaDesconto(self, porcentagem):
        self.__desconto += porcentagem/100
    
    def diminuiDesconto(self, porcentagem):
        self.__desconto -= porcentagem/100
    
    def retornaSobrenome(self):
        return ' '.join(self.__nome.split(' ')[1:])

    def retornaValorMensalidade(self):
        valor = 0
        for d in self.__disciplinas:
            valor += d.getMensalidade()
        return valor * self.__desconto

    def retornaCargaHorario(self):
        carga_horaria = 0
        for d in self.__disciplinas:
            carga_horaria += d.getCargaHoraria()
        return carga_horaria * 6

    
