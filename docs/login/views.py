from django.shortcuts import render, redirect
from .backend import autenticar


def entrar(request):
    contexto = {}
    if request.method == 'POST':
        if autenticar(request):
            return redirect('/')
    else:
        pass
    
    return render(request, 'login.html', contexto)
