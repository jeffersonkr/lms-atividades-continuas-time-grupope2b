from core.models.alunos import Aluno
from core.models.professores import Professor
from core.models.coordenadores import Coordenador
from django.core.exceptions import ObjectDoesNotExist
from core.models.sessaoAluno import SessaoAluno

def autenticar(request):
    emailusuario = request.POST.get('email')
    senhausuario = request.POST.get('senha')
    try:
        usuario = Aluno.objects.get(email=emailusuario)
        if senhausuario == usuario.senha:
            sessao = SessaoAluno.objects.create(usuarioAluno = usuario)
            request.sessao = sessao
            return True
        else:
            return False
    except:
        try:
            usuario = Professor.objects.get(email=emailusuario)
            if senhausuario == usuario.senha:
                return True
            else:
                return False
        except:
            try:
                usuario = Coordenador.objects.get(email=emailusuario)
                if senhausuario == usuario.senha:
                    return True
                else:
                    return False
            except ObjectDoesNotExist:
                return False

