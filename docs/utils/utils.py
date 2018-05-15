import datetime
from difflib import SequenceMatcher

def calculaMEdiaFinal(ac, Prova):
    media = 0.6 * ac + 0.4 * Prova
    return media

def geraNumeroRA(ultimoRA):
    matricula = str(ultimoRA)
    Ano = datetime.date.today().year
    AnoStr = str(Ano)
    if matricula[:2] == AnoStr[2:]:
        return int(AnoStr[2:]+matricula[2:])+1
    else:
        return int(AnoStr[2:]+'00000')+1
def calculaMedia(listaNotas):
    soma = 0
    for notas in listaNotas:
        soma += notas
    media = soma / len(listaNotas)
    return media

def descontaNota(nota, porcentagem):
    porcento = porcentagem/100
    notafinal = nota - nota*porcento
    return notafinal

def verificaCopia(texto1, texto2):
    var = int(SequenceMatcher(None, texto1, texto2).ratio())

    if(var >= 0.8):
        return True
    else:
        return False

