from enterprise_app.models import User, Cage, Facility
from poultry_farm_project.repositories import ORMRepository


class ORMUserRepository(ORMRepository):

    def __init__(self) -> None:
        super().__init__(User)


class ORMCageRepository(ORMRepository):

    def __init__(self) -> None:
        super().__init__(Cage)


class ORMFacilityRepository(ORMRepository):

    def __init__(self) -> None:
        super().__init__(Facility)
