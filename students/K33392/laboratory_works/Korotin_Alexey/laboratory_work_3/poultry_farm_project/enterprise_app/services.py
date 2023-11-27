from poultry_farm_project.services import DefaultCRUDService
from .repository.impl import ORMUserRepository, ORMCageRepository, ORMFacilityRepository


class UserService(DefaultCRUDService):
    def __init__(self):
        super().__init__(ORMUserRepository())


class CageService(DefaultCRUDService):
    def __init__(self):
        super().__init__(ORMCageRepository())


class FacilityService(DefaultCRUDService):
    def __init__(self):
        super().__init__(ORMFacilityRepository())
