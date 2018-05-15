from core.models.alunos import Aluno
from core.models.professores import Professor
from core.models.coordenadores import Coordenador
from django.core.exceptions import ObjectDoesNotExist
from core.models.sessaoAluno import SessaoAluno
from core.models.sessaoProfessor import SessaoProfessor
from core.models.sessaoCoordenador import SessaoCoordenador


def autenticar(request):
    emailusuario = request.POST.get('email')
    senhausuario = request.POST.get('senha')

    try:
        usuario = Aluno.objects.get(email=emailusuario)
        if senhausuario == usuario.senha:
            sessao = SessaoAluno.objects.create(usuarioaluno = usuario)
            request.sessao = sessao
            return True
        else:
            return False
    except:
        try:
            usuario = Professor.objects.get(email=emailusuario)
            if senhausuario == usuario.senha:
                sessao = SessaoProfessor.objects.create(usuarioprofessor = usuario)
                request.sessao = sessao
                return True
            else:
                return False
        except:
            try:
                usuario = Coordenador.objects.get(email=emailusuario)
                if senhausuario == usuario.senha:
                    sessao = SessaoCoordenador.objects.create(usuariocoordenador = usuario)
                    request.sessao = sessao
                    return True
                else:
                    return False

            except ObjectDoesNotExist:
                contexto = {
                    'erro': 'Usuário não existe'
                }
                return (False, contexto)

