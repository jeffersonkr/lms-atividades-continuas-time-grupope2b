from core.models.sessaoAluno import SessaoAluno
from core.models.sessaoProfessor import SessaoProfessor
from core.models.sessaoCoordenador import SessaoCoordenador
from django.shortcuts import redirect



class GuardaMiddleware(object):
    def __init__(self, get_response):
        self.get_response =get_response

    def __call__(self, request):
        if not request.path_info.startswith("/static/"):
            if request.path_info.startswith('/alunos/'):
                if not hasattr(request, 'sessao'):
                    return redirect('/login/')
            elif request.path_info.startswith('/professores/'):
                if not hasattr(request, 'sessao'):
                    return redirect('/login/')
            elif request.path_info.startswith('/adm/'):
                if not hasattr(request, 'sessao'):
                    return redirect('/login/')
            elif request.path_info.startswith('/coordenadores/'):
                if not hasattr(request, 'sessao'):
                    return redirect('/login/')
        response = self.get_response(request)
        return response


class AutorizacaoMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path_info.startswith("/static/"):
            if 'PYSESSAO' in request.COOKIES:
                cookie = request.COOKIES['PYSESSAO']
                try:
                    sessao = SessaoAluno.objects.get(id=cookie)
                    request.sessao = sessao
                except:
                    try:
                        sessao = SessaoProfessor.objects.get(id=cookie)
                        request.sessao = sessao
                    except:
                        try:
                            sessao = SessaoCoordenador.objects.get(id=cookie)
                            request.sessao = sessao
                        except:
                            return False


        response = self.get_response(request)

        return response


