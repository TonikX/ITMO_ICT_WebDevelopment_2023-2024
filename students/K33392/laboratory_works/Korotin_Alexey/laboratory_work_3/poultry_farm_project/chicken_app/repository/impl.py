from poultry_farm_project.repositories import ORMRepository
from chicken_app.models import Chicken, Breed, Diet


class ORMChickenRepository(ORMRepository):
    def __init__(self):
        super().__init__(Chicken)


class ORMBreedRepository(ORMRepository):
    def __init__(self):
        super().__init__(Breed)


class ORMDietRepository(ORMRepository):
    def __init__(self):
        super().__init__(Diet)
