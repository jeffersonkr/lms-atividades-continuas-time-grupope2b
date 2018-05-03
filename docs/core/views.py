from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def formulario(request):
    return render(request, 'formulario.html')



def cadastroAluno(request):
    return render(request, 'cadastroaluno.html')


