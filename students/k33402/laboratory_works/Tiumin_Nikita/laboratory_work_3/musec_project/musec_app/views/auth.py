import string
import random

from rest_framework.decorators import api_view, authentication_classes
from musec_app.serializers import UserAuthSerializer, TokenSerializer
from musec_app.models import User, ApiToken
from musec_app.responses import api_response
from musec_app.auth.authentication import AppTokenAuthentication
from django.contrib.auth.hashers import PBKDF2SHA1PasswordHasher as PasswordHasher


@api_view(['POST'])
def register(request):
    serializer = UserAuthSerializer(data=request.data)
    if not serializer.is_valid():
        return api_response.validation_error(serializer.errors)

    email = serializer.validated_data['email']
    password = serializer.validated_data['password']

    if User.objects.filter(email=email).count() > 0:
        return api_response.error('The user with given email is already registered', 422)

    hasher = PasswordHasher()

    user = User.objects.create(email=email, password=hasher.encode(password, hasher.salt()))
    user.save()

    return api_response.success()


@api_view(['POST'])
def login(request):
    serializer = UserAuthSerializer(data=request.data)
    if not serializer.is_valid():
        return api_response.validation_error(serializer.errors)

    email = serializer.validated_data['email']
    password = serializer.validated_data['password']

    user = User.objects.filter(email=email).first()

    hasher = PasswordHasher()
    if not hasher.verify(password, user.password):
        return api_response.unauthenticated()

    source = string.ascii_letters + string.digits
    token = ''.join((random.choice(source) for _ in range(128)))

    api_token = ApiToken(token=token, user=user)
    api_token.save()

    return api_response.payload(TokenSerializer({'token': token}).data)


@api_view(['POST'])
@authentication_classes([AppTokenAuthentication])
def logout(request):
    request.auth.delete()

    return api_response.success('Successfully logged out.')
