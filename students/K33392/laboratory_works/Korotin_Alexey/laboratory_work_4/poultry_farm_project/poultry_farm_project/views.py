from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from .services import CRUDService
from typing import Type


class BaseAPIView(APIView):

    permission_classes = (IsAuthenticated, )

    def __init__(self, service: CRUDService, serializer: Type[ModelSerializer],
                 mutate_serializer: Type[ModelSerializer] = None) -> None:
        super().__init__()
        self.service = service
        self.serializer = serializer
        self.mutate_serializer = mutate_serializer

    def get(self, request):
        entity = self.service.find_all()
        serializer = self.serializer(entity, many=True)
        return Response(serializer.data)

    def post(self, request):
        entity = request.data
        serializer = self.serializer(data=entity) if self.mutate_serializer is None \
            else self.mutate_serializer(data=entity)

        if serializer.is_valid(raise_exception=True):
            self.service.save(serializer)

        return Response(serializer.data, status=201)


class BaseExactAPIView(APIView):

    permission_classes = (IsAuthenticated, )

    def __init__(self, service: CRUDService, serializer: Type[ModelSerializer],
                 mutate_serializer: Type[ModelSerializer] = None) -> None:
        super().__init__()
        self.service = service
        self.serializer = serializer
        self.mutate_serializer = mutate_serializer

    def get(self, request, pk):
        entity = self.service.find_by_id(pk)
        if entity is None:
            return Response(status=404)
        serializer = self.serializer(instance=entity)
        return Response(serializer.data)

    def put(self, request, pk):
        entity = request.data
        existing = self.service.find_by_id(pk)
        if existing is None:
            return Response(status=404)

        serializer = self.serializer(data=entity, instance=existing) if self.mutate_serializer is None \
            else self.mutate_serializer(data=entity, instance=existing)

        if serializer.is_valid(raise_exception=True):
            self.service.save(serializer)

        return Response(serializer.data)

    def delete(self, request, pk):
        existing = self.service.find_by_id(pk)
        if existing is None:
            return Response(status=404)

        self.service.delete_by_id(pk)
        return Response(status=204)
