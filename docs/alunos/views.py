from django.shortcuts import render, redirect
from core.models.alunos import Aluno
# Create your views here.

def indexAlunos(request):
    contexto = {
        'alunos': Aluno.objects.all(),
        'title': 'Lista de alunos'
    }

    return render(request, 'indexalunos.html', contexto)

def cadastroAluno(request):
    contexto={}

    if request.POST:

        email = request.POST.get('email'),
        senha = request.POST.get('senha'),
        senha2 = request.POST.get('senha2'),

        if senha == senha2:
            Aluno.objects.create(
                nome = request.POST.get('nome'),
                email = request.POST.get('email'),
                celular = request.POST.get('celular'),
                idlogin = request.POST.get('idlogin'),
                senha = request.POST.get('senha'),
                dtexpiracao = request.POST.get('dataexpiracao'),
                ra = request.POST.get('ra'),
                foto = request.POST.get('foto'),
            )
            return redirect('/alunos/')
        else:
            contexto['erro']='Senhas não conferem!'

    return render(request, 'cadastroaluno.html', contexto)

def alterarAluno(request, id):
    contexto = {
        'title': 'Alterar aluno',
        'aluno': Aluno.objects.get(id=id)
    }

    if request.POST:
        a = Aluno.objects.get(id=id)
        senha = request.POST.get('senha'),
        senha2 = request.POST.get('senha2'),

        if senha == senha2:
            a = Aluno.objects.get(id=id)
            nome = request.POST.get('nome'),
            email = request.POST.get('email'),
            celular = request.POST.get('celular'),
            idlogin = request.POST.get('idlogin'),
            senha = request.POST.get('senha'),
            dtexpiracao = request.POST.get('dataexpiracao'),
            ra = request.POST.get('ra'),
            foto = request.POST.get('foto'),

            a.save()

            return redirect('/alunos/')

        else:
            contexto['erro'] = 'Senhas não conferem'
    
    return render(request, 'cadastroaluno.html', contexto)

def removerAluno(request, id):
    contexto = {
        'title': 'Lista de alunos',
        'alunos': Aluno.objects.all()
    }
    if request.method == 'GET':
        aluno = Aluno.objects.get(id=id).delete()

        return redirect('/alunos/')
    
    return render(request, 'indexalunos.html', contexto)
