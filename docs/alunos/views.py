from django.shortcuts import render, redirect
from core.models.alunos import Aluno
from utils.utils import geraNumeroRA
from core.models.professores import Professor
from core.models.mensagens import Mensagem
# Create your views here.

def indexAlunos(request):
    
    contexto = {
        'alunos': Aluno.objects.all(),
        'title': 'Lista de alunos',
        
    }

    return render(request, 'areadoaluno.html', contexto)

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
            return redirect('/alunos/')
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

            return redirect('/alunos/')

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

        return redirect('/alunos/')
    
    return render(request, 'indexalunos.html', contexto)

def areaDoAluno(request):
    contexto = {
       'title':'Área do aluno',
    }
    return render(request, 'areadoaluno.html', contexto)
    
def mensagensAluno(request):
    try:
        mensagens = Mensagem.objects.filter(idaluno=request.sessao.usuarioaluno.id)
        a = mensagens.filter(status='Respondida')
    except:
        mensagens = ''

    contexto = {
        'professores': Professor.objects.all(),
        'aluno': request.sessao.usuarioaluno.nome,
        'mensagens': a,
    }

    if request.POST:
        Mensagem.objects.create(
            idaluno = Aluno.objects.get(id=request.sessao.usuarioaluno.id),
            assunto = request.POST.get('assunto'),
            referencia = request.POST.get('referencia'),
            dtenvio = request.POST.get('dtenvio'),
            idprofessor = Professor.objects.get(id=request.POST.get('idprofessor')),
            conteudo = request.POST.get('conteudo'),
        )
        
        return redirect('/alunos/principal/')


    return render(request, 'mensagens.html', contexto)

def subPrincipal(request):
    contexto = {
        'aluno': request.sessao.usuarioaluno.nome
    }

    return render(request, 'index2.html', contexto)