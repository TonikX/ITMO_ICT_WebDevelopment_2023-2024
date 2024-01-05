import string
import random

from rest_framework.decorators import api_view, authentication_classes
from musec_app.serializers import UserSerializer, UserAuthSerializer, TokenSerializer
from musec_app.models import User, ApiToken, UserProfile, Playlist
from musec_app.responses import api_response
from musec_app.auth.authentication import AppTokenAuthentication
from django.contrib.auth.hashers import PBKDF2SHA1PasswordHasher as PasswordHasher


@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return api_response.validation_error(serializer.errors)

    data = serializer.validated_data

    if User.objects.filter(email=data['email']).count() > 0:
        return api_response.error('The user with given email is already registered', 422)

    hasher = PasswordHasher()

    #  todo transaction
    user = User.objects.create(email=data['email'], password=hasher.encode(data['password'], hasher.salt()))
    user.save()

    profile = UserProfile(
        first_name=data['first_name'],
        last_name=data['last_name'],
        patronymic=data['patronymic'],
        user=user
    )
    profile.save()

    Playlist.create_favorite_playlist_for_user(user)

    return api_response.payload(UserSerializer(user).data)


@api_view(['POST'])
def login(request):
    serializer = UserAuthSerializer(data=request.data)
    if not serializer.is_valid():
        return api_response.validation_error(serializer.errors)

    email = serializer.validated_data['email']
    password = serializer.validated_data['password']

    user = User.objects.filter(email=email).first()

    if not user:
        return api_response.not_found('User not found')

    hasher = PasswordHasher()
    if not hasher.verify(password, user.password):
        return api_response.unauthenticated()

    source = string.ascii_letters + string.digits
    token = ''.join((random.choice(source) for _ in range(128)))

    api_token = ApiToken(token=token, user=user)
    api_token.save()

    response = api_response.payload(TokenSerializer({'token': token}).data)
    response.set_cookie(
        key='api_token',
        value=token,
        httponly=True
    )

    return response


@api_view(['POST'])
@authentication_classes([AppTokenAuthentication])
def logout(request):
    request.auth.delete()

    return api_response.success('Successfully logged out.')
