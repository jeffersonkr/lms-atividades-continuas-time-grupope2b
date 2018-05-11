from django.shortcuts import render, redirect
from .backend import autenticar
def entrar(request):
    contexto = {
        'title': 'Área de login'
    }
    if request.method == 'POST':
        if autenticar(request):
            return redirect('/')
        else:
            contexto['erro'] = 'Usuario ou senha incorretos!'
    
    return render(request, 'login.html', contexto)

def sair(request):
    request.sessao.delete()
    return redirect('/')