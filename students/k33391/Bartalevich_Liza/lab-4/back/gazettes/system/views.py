from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from .models import  *
from rest_framework.decorators import action
from . import serializers
from .utils import get_tokens_for_user
from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.models import User


class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = serializers.AnimalSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]

    @action(detail=False, methods=["GET"])
    def animals_in_communas(self, request):
        aias = AnimalInAviary.objects.filter(aviary__communal=True)
        ser = serializers.ShowAnimalInAviarySerializer(aias, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["GET"])
    def in_the_same_aviary(self, request, pk=None):
        animal = self.get_object()
        qs = self.queryset.filter(where=animal.where)
        ser = self.serializer_class(qs, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


class OwningViewSet(ModelViewSet):
    queryset = Owning.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve', 'show_in_lease']:
            return serializers.ShowOwningSerializer
        return serializers.OwningSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]

    @action(detail=False, methods=["GET"])
    def show_in_lease(self, request):
        qs = Owning.objects.filter(in_lease=True)
        ser = self.get_serializer(qs, many=True)
        return Response(ser.data)

    
class AreaViewSet(ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = serializers.AreaSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]

    @action(detail=True, methods=["GET"])
    def count_animals_in(self, request, pk=None):
        obj = self.get_object()
        ser = serializers.CountAnimalInArea(obj)
        return Response(ser.data, status=status.HTTP_200_OK)


class AviaryViewSet(ModelViewSet):
    queryset = Aviary.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.ShowAviarySerializer
        return serializers.AviarySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]


    @action(detail=False, methods=["GET"])
    def show_empty(self, request):
        qs = Aviary.objects.none()

        for obj in Aviary.objects.all():
            if AnimalInAviary.objects.filter(aviary=obj.id).count() == 0:
                qs |= Aviary.objects.filter(id=obj.id)

        ser = serializers.AviarySerializer(qs, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)


class ZooViewSet(ModelViewSet):
    queryset = Zoo.objects.all()
    serializer_class = serializers.ZooSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]


class TypeOfDietViewSet(ModelViewSet):
    queryset = TypeOfDiet.objects.all()
    serializer_class = serializers.TypeOfDietSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]


class DietViewSet(ModelViewSet):
    queryset = Diet.objects.all()
    serializer_class = serializers.DietSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]


class HabitatViewSet(ModelViewSet):
    queryset = Habitat.objects.all()
    serializer_class = serializers.HabitatSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]


class WinterPlaceViewSet(ModelViewSet):
    queryset = WinterPlace.objects.all()
    serializer_class = serializers.WinterPlaceSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]


class AnimalInAviaryViewSet(ModelViewSet):
    queryset = AnimalInAviary.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return serializers.ShowAnimalInAviarySerializer
        return serializers.AnimalInAviarySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]


class WorkerViewSet(ModelViewSet):
    queryset = Worker.objects.all()
    serializer_class = serializers.WorkerSerializer


class RegistrationView(generics.CreateAPIView):
    serializer_class = serializers.RegistrationSerializer
    queryset = User.objects.all()


class LoginView(generics.GenericAPIView):
    serializer_class = serializers.LoginSerializer
    queryset = User.objects.all()

    def post(self, request):
        if 'username' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        print(username, password)
        if username is not None and password is not None:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                auth_data = get_tokens_for_user(request.user)
                return Response({'msg': 'Login Success', **auth_data}, status=status.HTTP_200_OK)
            return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    serializer_class = serializers.LogoutSerializer
    queryset = User.objects.all()

    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)


class ChangePasswordView(generics.GenericAPIView):
    serializer_class = serializers.PasswordChangeSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        request.user.set_password(serializer.validated_data['new_password'])
        request.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
