from django.db import models
from .value_objects import Location


class Worker(models.Model):
    passport = models.CharField(max_length=10)
    salary = models.IntegerField()
    employment_contract_id = models.IntegerField()
    dismissal_agreement_id = models.IntegerField()

    def __str__(self):
        return self.passport


class Facility(models.Model):
    name = models.CharField(max_length=255)
    _longitude = models.FloatField()
    _latitude = models.FloatField()

    @property
    def location(self) -> Location:
        return Location(self._longitude, self._latitude)

    @location.setter
    def location(self, value: Location) -> None:
        self._longitude = value.longitude
        self._latitude = value.latitude

    def __str__(self):
        return self.name


class Cage(models.Model):
    facility = models.ForeignKey(Facility, on_delete=models.DO_NOTHING)
    row = models.IntegerField()
    column = models.IntegerField()
    responsible = models.ForeignKey(Worker, on_delete=models.DO_NOTHING)
