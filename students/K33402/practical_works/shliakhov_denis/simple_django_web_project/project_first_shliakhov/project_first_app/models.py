from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Owner(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birthday = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.first_name.capitalize() + " " + self.last_name.capitalize()


class Car(models.Model):
    state_number = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True, blank=True)
    use = models.ManyToManyField(settings.AUTH_USER_MODEL, through="Ownership")

    def __str__(self) -> str:
        return self.brand.capitalize() + " " + self.model.capitalize()


class License(models.Model):
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    number_license = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    date_issue = models.DateField()

    def __str__(self) -> str:
        return self.number_license


class Ownership(models.Model):
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.start_date.__str__() + " to " + self.end_date.__str__()