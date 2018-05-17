from django.shortcuts import render, redirect
from utils.utils import geraNumeroRA
from core.models.alunos import Aluno
from core.models.professores import Professor

# Create your views here.
def index(request):
    contexto = {
        'title': 'C R U D'
    }
    return render(request, 'adm.html', contexto)

def listarAluno(request):
    contexto = {
        'title': 'Lista de alunos',
        'alunos': Aluno.objects.all(),
    }
    return render(request, 'indexalunos.html', contexto)

def cadastroAluno(request):
    try:
        ra = geraNumeroRA(Aluno.objects.latest("id").ra)
    except:
        ra = geraNumeroRA(000000)
    contexto={
        'geradorra': ra
    }
    
    if request.POST:
        senha = request.POST.get('senha'),
        senha2 = request.POST.get('senha2'),

        if senha == senha2:
            Aluno.objects.create(
                nome = request.POST.get('nome'),
                email = request.POST.get('email'),
                celular = request.POST.get('celular'),
                idlogin = request.POST.get('idlogin'),
                senha = request.POST.get('senha'),
                dtexpiracao = request.POST.get('dataexpiracao'),
                ra = request.POST.get('ra'),
                foto = request.POST.get('foto'),
            )
            return redirect('/adm/alunos/')
        else:
            contexto['erro']='Senhas não conferem!'

    return render(request, 'cadastroaluno.html', contexto)

def alterarAluno(request, id):
    contexto = {
        'title': 'Alterar aluno',
        'aluno': Aluno.objects.get(id=id),
        'geradorra': Aluno.objects.get(id=id).ra,
    }

    if request.POST:
        a = Aluno.objects.get(id=id)
        senha = request.POST.get('senha'),
        senha2 = request.POST.get('senha2'),

        if senha == senha2:

            a = Aluno.objects.get(id=id)
            a.nome = request.POST.get('nome')
            a.email = request.POST.get('email')
            a.celular = request.POST.get('celular')
            a.idlogin = request.POST.get('idlogin')
            a.senha = request.POST.get('senha')
            a.dtexpiracao = request.POST.get('dataexpiracao')
            a.ra = request.POST.get('ra')
            a.foto = request.POST.get('foto')

            a.save()

            return redirect('/adm/alunos/')

        else:
            contexto['erro'] = 'Senhas não conferem'
    
    return render(request, 'cadastroaluno.html', contexto)

def removerAluno(request, id):
    contexto = {
        'title': 'Lista de alunos',
        'alunos': Aluno.objects.all()
    }
    if request.method == 'GET':
        aluno = Aluno.objects.get(id=id).delete()

        return redirect('/adm/alunos/')
    
    return render(request, 'indexalunos.html', contexto)

def listaProfessor(request):
    contexto = {
        'professores': Professor.objects.all()
    }
    return render(request, 'indexProfessor.html', contexto)


def cadastrarProfessor(request):
    contexto={}

    if request.POST:
        
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')
        if senha == senha2:
            Professor.objects.create(
                nome = request.POST.get('nome'),
                email = request.POST.get('email'),
                celular = request.POST.get('celular'),
                idlogin = request.POST.get('idlogin'),
                senha = request.POST.get('senha'),
                dtexpiracao = request.POST.get('dataexpiracao'),
                apelido = request.POST.get('apelido'),
                
            )
            return redirect('/adm/professores/')

        else:
            contexto['erro']= 'Senhas não conferem!'
    else:
        return render(request, 'cadastroProfessor.html', contexto)

def removerProfessor(request, id):
    contexto={
        'title': 'Remover professor',
        'professores': Professor.objects.all(),
    }

    if request.method == 'GET':
        professor = Professor.objects.get(id=id).delete()

        return redirect('/adm/professores/')

    return render(request, 'indexProfessor.html', contexto)

def alterarProfessor(request, id):
    contexto = {
        'title': 'Alterar Professor',
        'professor': Professor.objects.get(id=id)
    }

    if request.POST:
        senha = request.POST.get('senha')
        senha2 = request.POST.get('senha2')

        if senha == senha2:
            professor = Professor.objects.get(id=id)

            professor.nome = request.POST.get('nome'),
            professor.email = request.POST.get('email'),
            professor.celular = request.POST.get('celular'),
            professor.idlogin = request.POST.get('idlogin'),
            professor.senha = request.POST.get('senha'),
            professor.dtexpiracao = request.POST.get('dataexpiracao'),
            professor.apelido = request.POST.get('apelido'),

            professor.save()

            return redirect('/professores/')
        else:
            contexto['erro']= 'Senhas não conferem!'
    
    return render(request, 'cadastroProfessor.html', contexto)
