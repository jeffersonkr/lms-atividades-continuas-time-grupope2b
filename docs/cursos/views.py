from django.shortcuts import render, redirect
from core.models.cursos import Curso
from django.http import HttpResponse

def listaCursos(request):
    contexto={
        'cursos': Curso.objects.all()
    }
    return render(request, 'lista_cursos.html', contexto)

def incluirCurso(request):
    contexto ={}

    if request.POST:
        Curso.objects.create(
            nome = request.POST.get('nome'),
            sigla = request.POST.get('sigla')
        )

        return redirect('/cursos/novoCurso/')
    else:
        return render(request, 'formCurso.html', contexto)


def alterarCurso(request, id):
    contexto ={}

    if request.POST:
        curso = Curso.objects.get(id=id)
        
        curso.nome = request.POST.get('nome')
        
        curso.save()

    return redirect('/curso/novoCurso/')


