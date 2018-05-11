from django.shortcuts import render, redirect
from core.models.cursos import Curso
from core.models.disciplinas import Disciplina
from core.models.coordenadores import Coordenador
from django.forms import Form

def listarDisciplinas(request):
    contexto={
        'disciplinas':Disciplina.objects.all(),
        'title': 'Lista de disciplinas'
    }
    return render(request, 'lista_disciplinas.html', contexto)

def incluirDisciplinas(request):
    contexto ={
        'coordenadores': Coordenador.objects.all(),
        'title': 'Incluir disciplinas'
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
    contexto ={}

def removerDisciplina(request, id):
    contexto = {
        'title': 'Disciplinas',
        'disciplina': Disciplina.objects.get(id=id),
    }

    if request.method == 'GET':
        disciplina = Disciplina.objects.get(id=id).delete()
        
        return redirect('/disciplinas/')

    return render(request, 'lista_disciplinas.html', contexto)


