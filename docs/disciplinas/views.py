from django.shortcuts import render, redirect
from core.models.cursos import Curso
from core.models.disciplinas import Disciplina


def listarDisciplinas(request):
    contexto={
        'disciplinas':Disciplina.objects.all()
    }
    return render(request, 'lista_disciplinas.html', contexto)


def incluirDisciplinas(request):
    contexto ={
        'cursos': Cursos.objects.all()
    }

    if request.POST:
        curso = Cursos.objects.get(id=request.POST.get('curso'))
        Disciplina.objects.create(
            nome = request.POST.get('nome'),
            nomecurso = request.POST.get('nomecurso'),
            curso = curso
        )

        return redirect('/disciplinas/')
    else:
        return render(request, 'formDisciplina.html', contexto)

def alterarDisciplinas(request, id):
    contexto ={
        'cursos': Cursos.objects.all()
    }

    if request.POST:
        curso = Cursos.objects.get(id=request.POST.get('curso'))
        disciplina = Disciplina.objects.get(id=id)
       
        disciplina.nome = request.POST.get('nome')
        disciplina.nomecurso = request.POST.get('nomecurso')
        disciplina.curso = curso
        
        disciplina.save()
        return redirect('/disciplinas/')
    else:
        contexto ["disciplina"]=Disciplina.objects.get(id=id)
        return render(request, 'formDisciplina.html', contexto)


