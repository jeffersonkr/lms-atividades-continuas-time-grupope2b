from django.shortcuts import render

def listaUsuarios(request):
    return render(request, 'listaUsuarios.html')

def novoUsuario(request):
    return render(request, 'formUsuario.html')

def login(request):
    return render(request, 'login.html')