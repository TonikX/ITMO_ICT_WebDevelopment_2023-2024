from .services import UserService, FacilityService, CageService
from .serializers import UserSerializer, FacilitySerializer, CageSerializer, CageMutateSerializer
from poultry_farm_project.views import BaseAPIView, BaseExactAPIView
from rest_framework.decorators import api_view, permission_classes
from poultry_farm_project.permissions import IsDirectorPermission
from rest_framework.response import Response


class UserAPIView(BaseAPIView):

    def __init__(self):
        super().__init__(UserService(), UserSerializer)


class UserExactAPIView(BaseExactAPIView):

    def __init__(self):
        super().__init__(UserService(), UserSerializer)


class FacilityAPIView(BaseAPIView):

    def __init__(self):
        super().__init__(FacilityService(), FacilitySerializer)


class FacilityExactAPIView(BaseExactAPIView):

    def __init__(self):
        super().__init__(FacilityService(), FacilitySerializer)


class CageAPIView(BaseAPIView):

    def __init__(self):
        super().__init__(CageService(), CageSerializer, CageMutateSerializer)


class CageExactAPIView(BaseExactAPIView):

    def __init__(self):
        super().__init__(CageService(), CageSerializer, CageMutateSerializer)


@api_view(["GET"])
@permission_classes([IsDirectorPermission])
def chickens_by_breed_in_facilities(request) -> Response:
    service = FacilityService()
    data = service.get_chickens_by_breed()

    return Response(data=data, status=200)


@api_view(["GET"])
@permission_classes([IsDirectorPermission])
def average_eggs_by_worker(request) -> Response:
    service = CageService()
    data = service.get_average_by_worker()

    return Response(data=data, status=200)


@api_view(["GET"])
@permission_classes([IsDirectorPermission])
def report(request) -> Response:
    service = FacilityService()
    data = service.report()
    return Response(data=data, status=200)