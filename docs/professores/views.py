from django.shortcuts import render, redirect
from core.models.alunos import Aluno
from utils.utils import geraNumeroRA
from core.models.professores import Professor
from core.models.mensagens import Mensagem


def areaProfessor(request):
    contexto = {
        'professores': Professor.objects.all()
    }
    return render(request, 'areadoprofessor.html', contexto)

def mensagemProfessor(request):
   
    try:
        mensagens = Mensagem.objects.filter(idprofessor=request.sessao.usuarioprofessor.id).filter(status='Enviado')
        a = Mensagem.objects.filter(idprofessor=request.sessao.usuarioprofessor.id).filter(status='Enviada').count()

    except:
        mensagens = ''

    contexto = {
        'professor': request.sessao.usuarioprofessor.nome,
        'mensagens': mensagens,
        'qtdmensagens': a,
    }
    
    if request.POST:
        idmsg = request.POST.get('idmsg')
        msg = Mensagem.objects.get(id=idmsg)
        msg.status = 'Respondida'
        msg.resposta = request.POST.get('resposta')
        msg.dtresposta = request.POST.get('dtresposta')

        msg.save()

        return redirect('/professores/msgprofessor/')


    return render(request, 'msgprofessor.html', contexto)

def subPrincioalProf(request):
    contexto = {
        'professor': request.sessao.usuarioprofessor.nome
    }
    return render(request, 'index2prof.html',contexto)