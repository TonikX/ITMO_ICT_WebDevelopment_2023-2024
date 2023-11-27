from poultry_farm_project.services import DefaultCRUDService
from chicken_app.repository.impl import ORMChickenRepository, ORMBreedRepository, ORMDietRepository


class ChickenService(DefaultCRUDService):
    def __init__(self):
        super().__init__(ORMChickenRepository())


class BreedService(DefaultCRUDService):
    def __init__(self):
        super().__init__(ORMBreedRepository())


class DietService(DefaultCRUDService):
    def __init__(self):
        super().__init__(ORMDietRepository())

