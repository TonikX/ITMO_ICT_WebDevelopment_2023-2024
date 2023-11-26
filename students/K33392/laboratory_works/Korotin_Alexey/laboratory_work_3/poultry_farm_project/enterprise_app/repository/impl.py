from enterprise_app.models import Worker, Cage, Facility
from enterprise_app.repository import ORMRepository


class ORMWorkerRepository(ORMRepository):
    model = Worker


class ORMCageRepository(ORMRepository):
    model = Cage


class ORMFacilityRepository(ORMRepository):
    model = Facility
