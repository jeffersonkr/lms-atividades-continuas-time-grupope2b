from django.shortcuts import render, redirect
from curriculo.models import Cursos

def listaCursos(request):
    contexto={
        'cursos':Cursos.objects.all()
    }
    return render(request, 'lista_cursos.html', contexto)

def incluirCurso(request):
    contexto ={}

    if request.POST:
        Cursos.objects.create(
            nome = request.POST.get('nome'),
            sigla = request.POST.get('sigla'),
        )

        return redirect('/cursos/novoCurso/')
    else:
        return render(request, 'formCurso.html', contexto)


def alterarCurso(request, id):
    contexto ={}

    if request.POST:
        curso = Cursos.objects.get(id=id)
        
        curso.nome = request.POST.get('nome')
        curso.sigla = request.POST.get('sigla')
        
        curso.save()

    return redirect('/cursos/novoCurso/')


