from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def graduacao(request):
    return render(request, 'graduacao.html')

def adm(request):
    return render(request, 'adm.html')

def bd(request):
    return render(request, 'bd.html')

def jogosdigitais(request):
    return render(request, 'jogosdigitais.html')

def gti(request):
    return render(request, 'gti.html')

def ads(request):
    return render(request, 'ads.html')
