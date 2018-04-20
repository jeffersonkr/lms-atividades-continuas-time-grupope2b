from disciplina import Disciplina
from professor import Professor
from aluno import Aluno

def main():
    p1 = Professor('Jefferson Dong Min Kwak', 'jeffersonkr@hotmail.com', '1701391', '941040588')
    
    aluno1 = Aluno('Marcos Viana', 'marcosv@hotmail.com', '170100', '944440000', 0.10)
    
    ADS = Disciplina('Analise e Desenvolvimento de Sistemas', 40, 150, p1)

    ADS2 = Disciplina('Analise e Desenvolvimento de Sistemas2', 40, 150, p1)

    aluno1.adicionaDisciplina(ADS)
    p1.adicionaDisciplina(ADS)
    p1.adicionaDisciplina(ADS2)
    

    print(f'{aluno1.retornaCargaHorario():.0f} horas por semestre')
    print(f'{aluno1.retornaSobrenome()}')
    aluno1.aumentaDesconto(50)
    print(f'{aluno1.retornaValorMensalidade():.2f} por mes')


if __name__ == "__main__":
    main()