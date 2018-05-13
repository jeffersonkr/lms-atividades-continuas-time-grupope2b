from django.shortcuts import render, redirect
from .backend import autenticar
from core.models.sessoes import Sessao

def entrar(request):
    contexto = {
        'title': 'Área de login',
    }
    if request.POST:
        if autenticar(request):
            resposta = redirect('/')
            resposta.set_cookie('PYSESSAO', request.sessao.id)
            return resposta
        else:
            contexto['erro'] = 'Usuario ou senha incorretos!'
    
    return render(request, 'login.html', contexto)

def sair(request):
    sessao = request.sessao
    resposta = redirect('/')
    resposta.delete_cookie('PYSESSAO')
    sessao.delete()
    return resposta