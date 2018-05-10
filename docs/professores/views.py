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
        return redirect('/professores/cadastrarProfessor')
    else:
        return render(request, 'cadastroProfessor.html', contexto)