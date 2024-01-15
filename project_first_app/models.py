from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class AutoOwner(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    birth_date = models.DateTimeField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Auto(models.Model):
    state_number = models.CharField(max_length=15, blank=False)
    brand = models.CharField(max_length=20, blank=False)
    model = models.CharField(max_length=20, blank=False)
    colour = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.model} {self.state_number}'


class Licence(models.Model):
    owner = models.ForeignKey(AutoOwner, on_delete = models.CASCADE)
    licence_number = models.CharField(max_length=10, blank=False)
    type = models.CharField(max_length=10, blank=False)
    date_of_issue = models.DateField(blank=False)

    def __str__(self):
        return f'{self.licence_number} {self.type}'

class Ownership(models.Model):
    owner = models.ForeignKey(AutoOwner, on_delete = models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete = models.CASCADE)
    start_date = models.DateField(blank=False)
    end_date = models.DateField(blank=False)

    def __str__(self):
        return f'{self.owner} {self.auto} {self.start_date} {self.end_date}'