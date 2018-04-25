from django.http import HttpResponseRedirect
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.models import AnonymousUser
from django.utils.deprecation import MiddlewareMixin
from rest_framework.request import Request
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


def get_user_jwt(request):
    user = None
    try:
        user_jwt = JSONWebTokenAuthentication().authenticate(Request(request))
        if user_jwt is not None:
            user = user_jwt[0]
    except Exception as e:
        raise e

    return user or AnonymousUser()


class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.path.startswith('/admin/'):
            request.user = SimpleLazyObject(lambda : get_user_jwt(request))



class AuthRequiredMiddleware(MiddlewareMixin):
    def process_request(self, request):
        redirect_url = '/admin/login'

        if not request.user.is_authenticated() and request.path != redirect_url:
            return HttpResponseRedirect(redirect_url)
        return None