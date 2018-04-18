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