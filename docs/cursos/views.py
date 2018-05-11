from django.shortcuts import render, redirect
from core.models.cursos import Curso
from django.http import HttpResponse

def listaCursos(request):
    contexto={
        'title': 'Listagem de cursos',
        'cursos': Curso.objects.all()
    }
    return render(request, 'lista_cursos.html', contexto)

def incluirCurso(request):
    contexto ={
        'title': 'Incluir cursos'
    }

    if request.POST:
        Curso.objects.create(
            nome = request.POST.get('nome'),
            sigla = request.POST.get('sigla')
        )

        return redirect('/cursos/novoCurso/')
    else:
        return render(request, 'formCurso.html', contexto)


def alterarCurso(request, id):
    contexto ={
        'cursos': Curso.objects.get(id=id),
        'title': 'Alterar cursos'
    }

    
    if request.POST:
        curso = Curso.objects.get(id=id)
    
        curso.nome = request.POST.get('nome')
        curso.sigla = request.POST.get('sigla')
        
        curso.save()

        return redirect('/cursos/')
    
    return render(request, 'formCurso.html', contexto)


def removerCurso(request, id):
    contexto = {
        'cursos': Curso.objects.all(),
        'title': 'Lista de cursos'
    }
    
    if request.method == 'GET':
        a = Curso.objects.filter(id=id).delete()
  
        return redirect('/cursos/')

    return render(request, 'lista_cursos.html', contexto)
