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
    
def mensagensAluno(request):
    try:
        mensagens = Mensagem.objects.filter(idaluno=request.sessao.usuarioaluno.id).filter(status='Respondida')
        a = Mensagem.objects.filter(idaluno=request.sessao.usuarioaluno.id).filter(status='Respondida').count()

    except:
        mensagens = ''

    contexto = {
        'professores': Professor.objects.all(),
        'aluno': request.sessao.usuarioaluno.nome,
        'mensagens': mensagens,
        'qtdmensagens': a,
    }

    if request.POST:
        Mensagem.objects.create(
            idaluno = Aluno.objects.get(id=request.sessao.usuarioaluno.id),
            assunto = request.POST.get('assunto'),
            status = 'Enviado',
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

    return render(request, 'principal.html', contexto)