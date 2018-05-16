from django.shortcuts import render, redirect
from core.models.alunos import Aluno
from utils.utils import geraNumeroRA
from core.models.professores import Professor
from core.models.mensagens import Mensagem


def listaProfessor(request):
    contexto = {
        'professores': Professor.objects.all()
    }
    return render(request, 'areadoprofessor.html', contexto)


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
            return redirect('/professores/')

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

        return redirect('/professores/')

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

def areaDoProfessor(request):
    contexto={
        'titulo': 'Area do Professor',
    }
    return render(request, 'areadoprofessor.html', contexto)

def mensagemProfessor(request):
   
    try:
        mensagens = Mensagem.objects.filter(idProfessor=request.sessao.usuarioprofessor.id)
        a = mensagens.objects.filter(status='Respondida')
    except:
        mensagens = ''

    contexto = {
        'alunos': Aluno.objects.all(),
        'professor': request.sessao.usuarioprofessor.nome,
        'mensagens': a,
    }

    if request.POST:
        Mensagem.objects.create(
            idprofessor = Aluno.objects.get(id=request.sessao.usuarioprofessor.id),
            assunto = request.POST.get('assunto'),
            referencia = request.POST.get('referencia'),
            dtenvio = request.POST.get('dtenvio'),
            idaluno = Professor.objects.get(id=request.POST.get('idaluno')),
            conteudo = request.POST.get('conteudo'),
        )
        
        return redirect('/professores/principalprofessor/')


    return render(request, 'msgprofessor.html', contexto)

def subPrincioalProf(request):
    return render(request, 'index2prof.html')