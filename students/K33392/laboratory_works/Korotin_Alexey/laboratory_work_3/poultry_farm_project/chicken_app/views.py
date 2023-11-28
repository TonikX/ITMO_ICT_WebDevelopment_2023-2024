from .services import ChickenService, BreedService, DietService
from .serializers import ChickenSerializer, BreedSerializer, DietSerializer
from poultry_farm_project.views import BaseAPIView, BaseExactAPIView
from rest_framework.decorators import api_view, permission_classes
from poultry_farm_project.permissions import IsDirectorPermission
from rest_framework.response import Response


class ChickenAPIView(BaseAPIView):
    def __init__(self):
        super().__init__(ChickenService(), ChickenSerializer)


class ChickenExactAPIView(BaseExactAPIView):
    def __init__(self):
        super().__init__(ChickenService(), ChickenSerializer)


class BreedAPIView(BaseAPIView):
    def __init__(self):
        super().__init__(BreedService(), BreedSerializer)


class BreedExactAPIView(BaseExactAPIView):
    def __init__(self):
        super().__init__(BreedService(), BreedSerializer)


class DietAPIView(BaseAPIView):
    def __init__(self):
        super().__init__(DietService(), DietSerializer)


class DietExactAPIView(BaseExactAPIView):
    def __init__(self):
        super().__init__(DietService(), DietSerializer)


@api_view(["GET"])
@permission_classes([IsDirectorPermission])
def get_differences_by_breed(request):
    service = ChickenService()
    data = service.diff_between_average_by_breed()

    return Response(data=data, status=200)
