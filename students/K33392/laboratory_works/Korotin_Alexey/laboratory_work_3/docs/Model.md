# Модель 
Модель всего проекта была разбита на 2 приложения:

- chicken_app

- enterprise_app

## Chicken_app
```python
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
    cage = models.ForeignKey(Cage, on_delete=models.DO_NOTHING)
```

# Enterprise_app
```python
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
```
В enterprise_app был выделен value object `Location`, который представляет собой координаты точки. 

Класс предоставляет валидацию передаваемых значений при помощи метода `__post_init__`. 
Также класс в себе логику расчета расстояния между двумя координатами.

`value_objects.py`
```python
from dataclasses import dataclass
from .exceptions import LocationException

from math import pi, atan2, cos, sin, sqrt


@dataclass(frozen=True)
class Location:
    longitude: float
    latitude: float

    """
        Radian value of longitude
    """
    @property
    def longitude_rad(self) -> float:
        return self.longitude * pi / 180

    """
        Radian value of latitude
    """
    @property
    def latitude_rad(self) -> float:
        return self.longitude * pi / 180

    def __post_init__(self):
        if not -180 < self.longitude < 180:
            raise LocationException("Longitude value should be in range [-180, 180]")

        if not -90 < self.latitude < 90:
            raise LocationException("Latitude value should be in range [-90, 90]")

    """
        Calculate distance between two locations in meters
    """
    def distance_to(self, other: "Location") -> float:
        r = 6_371_000  # Earth radius in meters
        phi_1 = self.latitude_rad
        phi_2 = other.latitude_rad

        delta_phi = (other.latitude - self.latitude) * pi / 180
        delta_lambda = (other.longitude - self.latitude) * pi / 180

        a = sin(delta_phi / 2) ** 2 + cos(phi_1) * cos(phi_2) * sin(delta_lambda / 2) ** 2

        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return r * c  # distance between two locations in meters

    def __str__(self):
        return f"(longitude: {self.longitude}, latitude: {self.latitude})"
```
