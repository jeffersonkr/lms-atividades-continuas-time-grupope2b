from django.shortcuts import render, redirect
from core.models.coordenadores import Coordenador

# Create your views here.
def listacoordenador(request):
    contexto = {
        'title': 'Coordenadores',
        'coordenadores': Coordenador.objects.all(),
    }

    return render(request, 'indexcoordenador.html', contexto)

def incluirCoordenador(request):
    contexto = {
        'coordenadores': Coordenador.objects.all(),
        'title': 'Cadastro de coordenador',
    }
    if request.POST:
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')
        if senha == senha2:
            coordenador = Coordenador.objects.create(
                nome = request.POST.get('nome'),
                email = request.POST.get('email'),
                celular = request.POST.get('celular'),
                dtexpiracao = request.POST.get('dtexpiracao'),
                idlogin = request.POST.get('idlogin'),
                senha = request.POST.get('senha')
            )

            return redirect('/coordenadores/')

        else:
            contexto['erro']: 'Senhas não conferem.'

    return render(request, 'formcoordenador.html', contexto)

def alterarCoordernador(request, id):
    contexto = {
        'title': 'Alterar coordenador', 
        'coordenador': Coordenador.objects.get(id=id),
    }
    
    if request.POST:
        a = Coordenador.objects.get(id=id)
        senha = request.POST.get('senha'),
        senha2 = request.POST.get('senha2'),

        if senha == senha2:
            a = Coordenador.objects.get(id=id)
            a.nome = request.POST.get('nome')
            a.email = request.POST.get('email')
            a.celular = request.POST.get('celular')
            a.dtexpiracao = request.POST.get('dataexpiracao')
            a.idlogin = request.POST.get('idlogin')
            a.senha = request.POST.get('senha')
            a.save()

            return redirect('/coordenadores/')
        
        else:
            contexto['erro']: 'Senhas não conferem'

    return render(request, 'formcoordenador.html', contexto)

def removerCoordenador(request, id):
    contexto = {
        'coordenadores': Coordenador.objects.all()
    }

    if request.method == 'GET':
        a = Coordenador.objects.get(id=id).delete()

        return redirect('/coordenadores/')
    
    return render(request, 'indexcoordenador.html', contexto)