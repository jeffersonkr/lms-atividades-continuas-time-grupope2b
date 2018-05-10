from core.models.sessoes import Sessao

class AutorizacaoMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.path_info.startswith("/static/"):
            if self.sessionId in request.COOKIES:
                cookie = request.COOKIES[self.sessionId]
                sessao = Sessao.objects.get(id=cookie)
                request.sessao = sessao

        response = self.get_response(request)

        if hasattr(request, 'sessao'):
            response.set_cookie(self._sessionId, request.sessao.id)
        else:
            response.delete_cookie(self._sessionId)

        return response

        