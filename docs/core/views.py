from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def formulario(request):
    return render(request, 'formulario.html')

def listaCursos(request):
    contexto = {
        'cursos':[
            {'nome':'Administração de Empresas', 'link':'/curso/adm'},
            {'nome':'Analise e Desenvolvimento de Sistemas', 'link':'/curso/ads'},
            {'nome':'Banco de Dados', 'link':'/curso/db'},
            {'nome':'Gestão de Tecnologia da Informação', 'link':'/curso/gti'},
            {'nome':'Jogos Digitais', 'link':'/curso/db'},
        ]
    }
    return render(request, 'listaCursos.html', contexto)

def cadastroAluno(request):
    return render(request, 'cadastroaluno.html')


def detalheCurso(request):
    contexto = {
        'nome':'ANÁLISE E DESENVOLVIMENTO DE SISTEMAS',
        'sobre':'SOBRE O CURSO',
        'detalheCurso': '''Entender as necessidades das empresas é fundamental para fazê-las 
                                crescer e gerar bons resultados. Desta maneira, um dos caminhos para alavancar os negócios 
                                e se destacar no mercado de trabalho é o da Tecnologia. Para isso, a Faculdade Impacta oferece 
                                a graduação em Análise e Desenvolvimento de Sistemas, que prepara você para atuar em todas 
                                as etapas de projetos de tecnologia da informação - concepção, gerência e manutenção, 
                                aplicação e mensuração de resultados.

                                O curso é voltado para a criação de programas, softwares e sistemas para as empresas. As etapas 
                                do projeto de sistemas de software, como análise, projeto, teste, gestão, implantação e manutenção
                                de sistemas de informação também estão entre os aprendizados da graduação.'''
    }
    return render(request, 'detalhesCurso.html', contexto)