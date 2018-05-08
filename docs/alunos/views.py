from django.shortcuts import render, redirect
from core.models.alunos import Aluno

# Create your views here.
def cadastroAluno(request):
    contexto={}

    if request.POST:
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
        return redirect('/alunos/cadastroaluno')
    else:
        return render(request, 'cadastroaluno.html', contexto)