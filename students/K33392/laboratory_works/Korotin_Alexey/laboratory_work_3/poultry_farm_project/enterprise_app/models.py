from django.db import models
from django.contrib.auth.models import AbstractUser
from .value_objects import Location


class User(AbstractUser):
    ROLE_CHOICES = (
        ("W", "Worker"),
        ("D", "Director")
    )

    role = models.CharField(choices=ROLE_CHOICES, max_length=1)
    passport = models.CharField(max_length=10)
    salary = models.IntegerField()
    employment_contract_id = models.IntegerField()
    dismissal_agreement_id = models.IntegerField(null=True)

    REQUIRED_FIELDS = ["password", "role", "passport", "salary", "employment_contract_id"]

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
    responsible = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"row: {self.row}, column: {self.column}"
