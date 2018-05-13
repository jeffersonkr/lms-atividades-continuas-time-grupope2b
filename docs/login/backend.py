from core.models.alunos import Aluno
from core.models.professores import Professor
from core.models.coordenadores import Coordenador
from django.core.exceptions import ObjectDoesNotExist
from core.models.sessoes import Sessao

def autenticar(request):
    emailusuario = request.POST.get('email')
    senhausuario = request.POST.get('senha')

    try:
        if emailusuario == Aluno.objects.get(email=emailusuario):
            usuario = Aluno.objects.get(email=emailusuario)
            if senhausuario == usuario.senha:
                sessao = Sessao.objects.create(usuarioaluno = Aluno.objects.get(email = usuario.email))
                request.sessao = sessao
                return True
            else:
                return False
            
        elif emailusuario == Professor.objects.get(email=emailusuario):
            usuario = Professor.objects.get(email=emailusuario)
            if senhausuario == usuario.senha:
                sessao = Sessao.objects.create(usuarioprofessor = Professor.objects.get(email = usuario.email))
                request.sessao = sessao
                return True
            else:
                return False
        elif usuario == Coordenador.objects.get(email=emailusuario):
            usuario = Coordenador.objects.get(email=emailusuario)        
            if senhausuario == usuario.senha:
                sessao = Sessao.objects.create(usuariocoordenador = Coordenador.objects.get(email = usuario.email))
                request.sessao = sessao
                return True
            else:
                return False
    except ObjectDoesNotExist:
        contexto = {
            'erro': 'Usuário não existe'
        }
        return (False, contexto)

