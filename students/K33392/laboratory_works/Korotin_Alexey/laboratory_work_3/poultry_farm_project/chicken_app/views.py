from .services import ChickenService, BreedService, DietService
from .serializers import ChickenSerializer, BreedSerializer, DietSerializer
from poultry_farm_project.views import BaseAPIView, BaseExactAPIView


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
