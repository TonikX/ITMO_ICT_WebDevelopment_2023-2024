from django.db import models
from django.utils import timezone


class Driver(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birthdate = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} "


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


class Ownership(models.Model):
    owner_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateTimeField(blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.start_date:
            self.start_date = timezone.now()
        return super(Ownership, self).save(*args, **kwargs)
