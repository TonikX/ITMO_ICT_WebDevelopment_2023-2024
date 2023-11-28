from .services import UserService, FacilityService, CageService
from .serializers import UserSerializer, FacilitySerializer, CageSerializer
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
        super().__init__(CageService(), CageSerializer)


class CageExactAPIView(BaseExactAPIView):

    def __init__(self):
        super().__init__(CageService(), CageSerializer)


@api_view(["GET"])
@permission_classes([IsDirectorPermission])
def chickens_by_breed_in_facilities(request) -> Response:
    service = FacilityService()
    data = service.get_chickens_by_breed()

    return Response(data=data, status=200)
