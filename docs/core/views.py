from django.shortcuts import render

def home(request):
    contexto ={
        'title': 'Faculdade Impacta'
    }
    return render(request, 'index.html', contexto)

def graduacao(request):
    contexto ={
        'title': 'Graduação - Sobre o curso'
    }
    return render(request, 'graduacao.html', contexto)

def sobrecurso(request):

    return render(request, 'sobrecurso.html')


