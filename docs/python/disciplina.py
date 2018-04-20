class Disciplina:
    def __init__(self, nomedaDisciplina='', cargaHoraria=0, mensalidade=0.00, professor=None):
        self.__nomedaDisciplina = nomedaDisciplina
        self.__cargaHoraria = cargaHoraria
        self.mensalidade = mensalidade
        self.__professor = professor


    def getNomeDisciplina(self):
        return self.__nomedaDisciplina
    def setNomeDisciplina(self, nomedaDisciplina):
        self.__nomedaDisciplina = nomedaDisciplina

    def getCargaHoraria(self):
        return self.__cargaHoraria
    def setCargaHoraria(self, cargaHoraria):
        self.__cargaHoraria = cargaHoraria

    def getMensalidade(self):
        return self.mensalidade
    def setMensalidade(self, mensalidade):
        self.mensalidade = mensalidade

    def getProfessor(self):
        return self.__professor
    def setProfessor(self):
        self.__professor = professor

    def retornaValorHora(self):
        valorHora = (self.mensalidade * 6) / self.__cargaHoraria
        return valorHora
