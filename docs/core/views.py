from django.shortcuts import render

def home(request):
    contexto ={
        'title': 'Faculdade Impacta'
    }
    return render(request, 'index.html', contexto)

def graduacao(request):
    contexto ={
        'title': 'Graduação'
    }
    return render(request, 'graduacao.html', contexto)

def adm(request):
    contexto ={
        'title': 'Sobre curso'
    }
    return render(request, 'adm.html', contexto)

def bd(request):
    contexto ={
        'title': 'Sobre curso'
    }
    return render(request, 'bd.html', contexto)

def jogosdigitais(request):
    contexto ={
        'title': 'Sobre curso'
    }
    return render(request, 'jogosdigitais.html', contexto)

def gti(request):
    contexto ={
        'title': 'Sobre curso'
    }
    return render(request, 'gti.html', contexto)

def ads(request):
    contexto ={
        'title': 'Sobre curso'
    }
    return render(request, 'ads.html', contexto)




