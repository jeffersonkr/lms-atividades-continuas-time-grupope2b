from core.models.alunos import Aluno
from core.models.professores import Professor
from core.models.coordenadores import Coordenador
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

def autenticar(request):
    emailusuario = request.POST.get('email')
    senhausuario = request.POST.get('senha')
    try:
        usuario = Aluno.objects.get(email=emailusuario)
        if senhausuario == usuario.senha:
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
                pass

