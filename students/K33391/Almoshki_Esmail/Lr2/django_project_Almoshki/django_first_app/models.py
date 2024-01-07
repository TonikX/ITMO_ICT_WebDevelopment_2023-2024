from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# class User(AbstractUser):
#     name = models.CharField(max_length=100, blank=True, null=True)
#     passport_number = models.CharField(max_length=30, null=True, blank=True)
#     address = models.CharField(max_length=100, null=True, blank=True)
#     nationality = models.CharField(max_length=30, null=True, blank=True)


class Driver(AbstractUser):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birthdate = models.DateTimeField(null=True)
    passport_number = models.CharField(max_length=30)
    address = models.CharField(max_length=255)
    nationality = models.CharField(max_length=30)

    REQUIRED_FIELDS = ["passport_number", "address", "nationality"]

    def __str__(self):
        return f"{self.username} + ' ' + {self.nationality} + ' ' + {self.address} + ' ' + {self.passport_number} "


class DivingLicense(models.Model):
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    issue_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Licence number {self.license_number}"


class Car(models.Model):
    governmental_number = models.CharField(max_length=15)
    stamp = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self) -> str:
        return f"Car is {self.model} holding number {self.governmental_number}"


class Ownership(models.Model):
    owner_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.start_date:
            self.start_date = timezone.now()
        return super(Ownership, self).save(*args, **kwargs)
