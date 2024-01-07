from django.db import models
from enterprise_app.models import Cage


class Diet(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=255)
    average_monthly_egg_rate = models.IntegerField()
    average_weight = models.IntegerField()
    recommended_diet = models.ForeignKey(Diet, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Chicken(models.Model):
    weight = models.IntegerField()
    birth_date = models.DateField()
    monthly_egg_rate = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.DO_NOTHING)
    cage = models.ForeignKey(Cage, on_delete=models.DO_NOTHING, related_name="cage_chicken")

    def __str__(self):
        pass
