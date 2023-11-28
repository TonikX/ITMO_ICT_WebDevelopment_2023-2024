from poultry_farm_project.services import DefaultCRUDService
from .repository.impl import ORMUserRepository, ORMCageRepository, ORMFacilityRepository
from .models import Cage, User
from django.db.models import Count, Avg


class UserService(DefaultCRUDService):
    def __init__(self):
        super().__init__(ORMUserRepository())


class CageService(DefaultCRUDService):
    def __init__(self):
        super().__init__(ORMCageRepository())

    def get_average_by_worker(self):
        average_eggs_per_worker = (
            User.objects.filter(cage__cage_chicken__isnull=False)  # Убедимся, что есть связанные куры
                .annotate(average_eggs=Avg('cage__cage_chicken__monthly_egg_rate'))
                .values('id', 'username', 'average_eggs')
        )

        return average_eggs_per_worker


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
