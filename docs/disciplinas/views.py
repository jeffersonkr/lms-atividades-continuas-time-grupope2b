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
            status = request.POST.get('status'),
            cargahoraria = request.POST.get('cargahoraria'),
            habilidades = request.POST.get('habilidades'),
            ementa = request.POST.get('ementa'),
            conteudoprogramatico = request.POST.get('conteudoprogramatico'),
            bibliografiabasica = request.POST.get('bibliografiabasica'),
            bibliografiacomplementar = request.POST.get('bibliografiacomplementar'),
            percentualpratico = request.POST.get('percentualpratico'),
            percentualteorico = request.POST.get('percentualteorico'),
            idcoordenador = Coordenador.objects.get(id=request.POST.get('idcoordenador'))
        )

        return redirect('/disciplinas/')
    else:
        return render(request, 'formDisciplina.html', contexto)

        
def alterarDisciplinas(request, id):
    contexto ={
        'disciplina': Disciplina.objects.get(id=id),
        'title': 'Alterar disciplina',
        'coordenadores': Coordenador.objects.all(),
    }
    
    if request.POST:
        a = Disciplina.objects.get(id=id)
        a.nome = request.POST.get('nome')
        a.data = request.POST.get('data')
        a.planodeensino = request.POST.get('planodeensino')
        a.cargahoraria = request.POST.get('cargahoraria')
        a.habilidades = request.POST.get('habilidades')
        a.ementa = request.POST.get('ementa')
        a.conteudoprogramatico = request.POST.get('conteudoprogramatico')
        a.bibliografiabasica = request.POST.get('bibliografiabasica')
        a.bibliografiacomplementar = request.POST.get('bibliografiacomplementar')
        a.percentualpratico = request.POST.get('percentualpratico')
        a.percentualteorico = request.POST.get('percentualteorico')
        a.idcoordenador = Coordenador.objects.get(id=request.POST.get('idcoordenador'))

        a.save()

        return redirect('/disciplinas/')

    return render(request, 'formDisciplina.html', contexto)


def removerDisciplina(request, id):
    contexto = {
        'title': 'Disciplinas',
        'disciplina': Disciplina.objects.get(id=id),
    }

    if request.method == 'GET':
        disciplina = Disciplina.objects.get(id=id).delete()
        
        return redirect('/disciplinas/')

    return render(request, 'lista_disciplinas.html', contexto)


