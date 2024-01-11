from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import SAFE_METHODS, IsAdminUser, IsAuthenticatedOrReadOnly
from . import serializers
from .models import  *


class ActionViewSet(ViewSet):
    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]
    
    @action(detail=False, methods=["GET"])
    def animals_in_communas(self, request):
        aias = AnimalInAviary.objects.filter(aviary__communal=True)
        ser = serializers.AnimalInAviarySerializer(aias, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["GET"])
    def in_the_same_aviary(self, request, pk=None):
        animal = Animal.objects.get(id=pk)
        qs = AnimalInAviary.objects.filter(where=animal.where)
        ser = serializers.AnimalInAviarySerializer(qs, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"])
    def show_in_lease(self):
        qs = Owning.objects.filter(in_lease=True)
        ser = serializers.OwningSerializer(qs, many=True)
        return ser.data

    @action(detail=False, methods=["GET"])
    def count_animals_in(self, request):
        ser = serializers.CountAnimalInArea(Area.objects.all(), many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"])
    def show_empty(self, request):
        qs = Aviary.objects.none()

        for obj in Aviary.objects.all():
            if AnimalInAviary.objects.filter(aviary=obj.id).count() == 0:
                qs |= Aviary.objects.filter(id=obj.id)

        ser = serializers.AviarySerializer(qs, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)



class AnimalViewSet(ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = serializers.AnimalSerializer

    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]

class OwningViewSet(ModelViewSet):
    queryset = Owning.objects.all()
    serializer_class = serializers.OwningSerializer

    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]

class ZooViewSet(ModelViewSet):
    queryset = Zoo.objects.all()
    serializer_class = serializers.ZooSerializer

    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]

class BuildingViewSet(ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = serializers.BuildingSerializer

    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]


class AreaViewSet(ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = serializers.AreaSerializer

    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]


class AviaryViewSet(ModelViewSet):
    queryset = Aviary.objects.all()
    serializer_class = serializers.AviarySerializer

    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]

    
    @action(detail=True, methods=["GET"])
    def show(self, request, pk=None):
        obj = Aviary.objects.get(id=pk)
        ser = serializers.ShowAviarySerializer(obj)
        return Response(ser.data)



class TypeOfDietViewSet(ModelViewSet):
    queryset = TypeOfDiet.objects.all()
    serializer_class = serializers.TypeOfDietSerializer

    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]



class DietViewSet(ModelViewSet):
    queryset = Diet.objects.all()
    serializer_class = serializers.DietSerializer

    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]


class HabitatViewSet(ModelViewSet):
    queryset = Habitat.objects.all()
    serializer_class = serializers.HabitatSerializer

    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]


class WinterPlaceViewSet(ModelViewSet):
    queryset = WinterPlace.objects.all()
    serializer_class = serializers.WinterPlaceSerializer

    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]


class AnimalInAviaryViewSet(ModelViewSet):
    queryset = AnimalInAviary.objects.all()
    serializer_class = serializers.AnimalInAviarySerializer

    def get_permissions(self):
        if self.action in SAFE_METHODS:
            return [IsAuthenticatedOrReadOnly()]
        return [IsAdminUser()]
