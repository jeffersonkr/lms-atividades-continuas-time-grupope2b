from django.shortcuts import render, redirect
from core.models.professores import Professor


def listaProfessor(request):
    contexto = {
        'professores': Professor.objects.all()
    }
    return render(request, 'indexProfessor.html', contexto)


def cadastrarProfessor(request):
    contexto={}

    if request.POST:
        Professor.objects.create(
            nome = request.POST.get('nome'),
            email = request.POST.get('email'),
            celular = request.POST.get('celular'),
            idlogin = request.POST.get('idlogin'),
            senha = request.POST.get('senha'),
            dtexpiracao = request.POST.get('dataexpiracao'),
            apelido = request.POST.get('apelido'),
            
        )
        return redirect('/professores/')
    else:
        return render(request, 'cadastroProfessor.html', contexto)

def removerProfessor(request, id):
    contexto={
        'title': 'Remover professor',
        'professores': Professor.objects.all(),
    }

    if request.method == 'GET':
        professor = Professor.objects.get(id=id).delete()

        return redirect('/professores/')

    return render(request, 'indexProfessor.html', contexto)

def alterarProfessor(request, id):
    contexto = {
        'title': 'Alterar Professor',
        'professor': Professor.objects.get(id=id)

    }

    if request.POST:
        professor = Professor.objects.get(id=id)

        nome = request.POST.get('nome'),
        email = request.POST.get('email'),
        celular = request.POST.get('celular'),
        idlogin = request.POST.get('idlogin'),
        senha = request.POST.get('senha'),
        dtexpiracao = request.POST.get('dataexpiracao'),
        apelido = request.POST.get('apelido'),

        professor.save()

        return redirect('/professores/')
    
    return render(request, 'cadastroProfessor.html', contexto)