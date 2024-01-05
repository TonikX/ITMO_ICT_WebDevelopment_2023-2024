from rest_framework.authentication import BaseAuthentication, get_authorization_header
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import exceptions
from musec_app.models import User, ApiToken


class AppTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        try:
            token = request.COOKIES['api_token']
            api_token = ApiToken.objects.filter(token=token).get()
        except KeyError:
            raise exceptions.AuthenticationFailed('Unauthenticated')
        except ObjectDoesNotExist:
            raise exceptions.AuthenticationFailed('Unauthenticated')

        return api_token.user, api_token

    def authenticate_header(self, request):
        return 'Token'
