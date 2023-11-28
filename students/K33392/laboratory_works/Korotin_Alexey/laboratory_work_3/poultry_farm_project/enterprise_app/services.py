from poultry_farm_project.services import DefaultCRUDService
from .repository.impl import ORMUserRepository, ORMCageRepository, ORMFacilityRepository
from .models import Facility, Cage
from django.db.models import Count


class UserService(DefaultCRUDService):
    def __init__(self):
        super().__init__(ORMUserRepository())


class CageService(DefaultCRUDService):
    def __init__(self):
        super().__init__(ORMCageRepository())


class FacilityService(DefaultCRUDService):
    def __init__(self):
        super().__init__(ORMFacilityRepository())

    def get_chickens_by_breed(self):
        breed_counts = (
            Cage.objects
                .values('facility__name', 'cage_chicken__breed__name')
                .annotate(breed_count=Count('cage_chicken__breed__name'))
                .order_by('facility__name', 'cage_chicken__breed__name')
        )

        grouped_by_facility = {}
        for entry in breed_counts:
            facility_name = entry['facility__name']
            breed_name = entry['cage_chicken__breed__name']
            breed_count = entry['breed_count']

            if facility_name not in grouped_by_facility:
                grouped_by_facility[facility_name] = {}

            grouped_by_facility[facility_name][breed_name] = breed_count

        out = {}
        for facility, breed_counts in grouped_by_facility.items():
            out[facility] = []
            for breed, count in breed_counts.items():
                out[facility].append({breed: count})

        return out
