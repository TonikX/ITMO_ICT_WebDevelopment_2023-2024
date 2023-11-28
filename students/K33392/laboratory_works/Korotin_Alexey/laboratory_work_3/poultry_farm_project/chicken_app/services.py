from poultry_farm_project.services import DefaultCRUDService
from chicken_app.repository.impl import ORMChickenRepository, ORMBreedRepository, ORMDietRepository
from .models import Breed, Chicken
from django.db.models import Avg


class ChickenService(DefaultCRUDService):
    def __init__(self):
        super().__init__(ORMChickenRepository())

    def diff_between_average_by_breed(self):
        overall_avg = Chicken.objects.aggregate(
            avg_weight=Avg('weight'),
            avg_egg_rate=Avg('monthly_egg_rate')
        )

        breed_stats = Breed.objects.values(
            'name', 'average_weight', 'average_monthly_egg_rate'
        )

        breed_differences = {}
        for stat in breed_stats:
            breed_name = stat['name']
            breed_weight = stat['average_weight']
            breed_egg_rate = stat['average_monthly_egg_rate']

            overall_avg_weight = overall_avg['avg_weight']
            overall_avg_egg_rate = overall_avg['avg_egg_rate']

            difference_weight = breed_weight - overall_avg_weight
            difference_egg_rate = breed_egg_rate - overall_avg_egg_rate

            breed_differences[breed_name] = {
                'difference_weight': difference_weight,
                'difference_egg_rate': difference_egg_rate
            }

        out = {}
        for breed, differences in breed_differences.items():
            out[breed] = {"weight": differences['difference_weight'],
                          "egg_rate": differences['difference_egg_rate']}

        return out


class BreedService(DefaultCRUDService):
    def __init__(self):
        super().__init__(ORMBreedRepository())


class DietService(DefaultCRUDService):
    def __init__(self):
        super().__init__(ORMDietRepository())

