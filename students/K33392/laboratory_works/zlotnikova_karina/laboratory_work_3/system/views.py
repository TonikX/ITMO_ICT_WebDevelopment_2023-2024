import math

from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ViewSet
from rest_framework import generics
from .utils import get_tokens_for_user
from .serializers import *
from .models import CustomUser, Product, Eaten
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from drf_spectacular.utils import extend_schema


class CountViewSet(ViewSet):
    @extend_schema(request=InCalculateSerializer, responses={"norm_of_calories": int}) #дока для сваггера (определяет как внешний вид и поля сваггера)
    @action(detail=False, methods=["POST"]) 
    def calculate(self, request):
        sex = request.data.get('sex', None)
        tall = request.data.get('tall', None)
        w = request.data.get('weight', None)
        age = request.data.get('age', None)
        res = 0
        if sex == 'female':
            res = ((10 * w) + (6.25 * tall) - (5 * age) - 161)
        elif sex == 'male':
            res = ((10 * w) + (6.25 * tall) - (5 * age) + 5)
        else:
            return Response('sex is not valid', status=status.HTTP_400_BAD_REQUEST)

        return Response({"norm_of_calories": math.ceil(res)}, status=status.HTTP_200_OK)


class ProfileViewSet(GenericViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["GET"])
    def me(self, request):
        obj = request.user
        ser = ProfileSerializer(obj)
        return Response(ser.data)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticated()] # сравнение токенов в бд и того, который пришел с запроса
        return [IsAdminUser()]


class EatenViewSet(GenericViewSet):
    queryset = Eaten.objects.all()
    serializer_class = CreateEatenSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request):
        ser = self.get_serializer(data=request.data, context={"user": request.user})
        if ser.is_valid():
            ser.save()
            return Response(status=status.HTTP_201_CREATED)

#########################


class RegistrationView(generics.CreateAPIView):
    serializer_class = RegistrationSerializer
    queryset = CustomUser.objects.all()


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    queryset = CustomUser.objects.all()

    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.data.get("email", None)
        password = request.data.get("password", None)
        if email is not None and password is not None:
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                auth_data = get_tokens_for_user(request.user)
                return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
            return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    serializer_class = LogoutSerializer
    queryset = CustomUser.objects.all()

    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)


class ChangePasswordView(generics.GenericAPIView):
    serializer_class = PasswordChangeSerializer
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True) #Another way to write is as in Line 17
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
