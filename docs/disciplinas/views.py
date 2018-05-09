from django.shortcuts import render, redirect
from core.models.cursos import Curso
from core.models.disciplinas import Disciplina
from core.models.coordenadores import Coordenador
from django.forms import Form

def listarDisciplinas(request):
    contexto={
        'disciplinas':Disciplina.objects.all()
    }
    return render(request, 'lista_disciplinas.html', contexto)

def incluirDisciplinas(request):
    contexto ={
        'coordenadores': Coordenador.objects.all()
    }

    if request.POST:
        Disciplina.objects.create(
            nome = request.POST.get('nome'),
            data = request.POST.get('data'),
            planodeensino = request.POST.get('planodeensino'),
            cargahoraria = request.POST.get('çargahoraria'),
            habilidades = request.POST.get('habilidades'),
            ementa = request.POST.get('ementa'),
            conteudoprogramatico = request.POST.get('conteudoprogramatico'),
            bibliografiabasica = request.POST.get('bibliografiabasica'),
            bibliografiacomplementar = request.POST.get('bibliografiacomplementar'),
            percentualpratico = request.POST.get('percentualpratico'),
            percentualteorico = request.POST.get('percentualteorico'),
            idcoordenador = request.POST.get('idcoordenador'),
        )

        return redirect('/disciplinas/novaDisciplina')
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


