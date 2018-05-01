from django.shortcuts import render, redirect
from curriculo.models import Cursos, Disciplina

def listaCursos2(request):
    contexto={
        'cursos':Cursos.objects.all()
    }
    return render(request, 'lista_cursos.html', contexto)

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

        return redirect('/Disciplinas/')
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
        return redirect('/Disciplinas/')
    else:
        contexto ["disciplina"]=Disciplina.objects.get(id=id)
        return render(request, 'formDisciplina.html', contexto)


def incluirCurso(request):
    contexto ={}

    if request.POST:
        Cursos.objects.create(
            nome = request.POST.get('nome'),
            sigla = request.POST.get('sigla'),
        )

        return redirect('/novoCurso/')
    else:
        return render(request, 'formCurso.html', contexto)


def alterarCurso(request, id):
    contexto ={}

    if request.POST:
        curso = Cursos.objects.get(id=id)
        
        curso.nome = request.POST.get('nome')
        curso.sigla = request.POST.get('sigla')
        
        curso.save()

    return redirect('/novoCurso/')


def curso(request,sigla):

    cursos = {
        'ADS':{ 'titulo': 'Analise de Desenvolvimento de Sistemas',
        'carga_horaria': '2020h'},
        
        'BD':{ 'titulo': 'Banco de dados',
        'carga_horaria': '2040h'}
    }

    curso = cursos[sigla]
    return render(request, 'cursoADS.html', curso)