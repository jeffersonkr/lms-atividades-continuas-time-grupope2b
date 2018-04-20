class Professor:
    def __init__(self, nome='', email='', ra='', celular=''):
        self.__nome = nome
        self.__email = email
        self.__ra = ra
        self.__celular = celular
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
    def setRa(self, ra):
        self.__ra = ra

    def getCelular(self):
        return self.__celular
    def setCelular(self, celular):
        self.__celular = celular

    def retornaSobrenome(self):
        return ' '.join(self.__nome.split(' ')[1:])

    def adicionaDisciplina(self, disciplina):
        if disciplina.getProfessor().getRa():
            self.__disciplinas.append(disciplina)
        else:
            return 'Professor não associado a disciplna'

    def retornaCargaHoraria(self):
        soma_carga = 0
        for d in self.__disciplinas:
            soma_carga += d.getCargaHoraria()
        return (soma_carga/20)*5