from .services import UserService, FacilityService, CageService
from .serializers import UserSerializer, FacilitySerializer, CageSerializer
from poultry_farm_project.views import BaseAPIView, BaseExactAPIView


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

