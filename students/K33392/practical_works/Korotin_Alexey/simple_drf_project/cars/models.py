from django.db import models


class Car(models.Model):
    license_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30)
    related_name = "car"

    def __str__(self):
        return f"Car(license_plate={self.license_plate}, brand={self.brand}, model={self.model}, color={self.color})"


class CarOwner(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    birth_date = models.DateTimeField(null=True)
    passport = models.CharField(max_length=10, null=True)
    home_Address = models.CharField(max_length=200, null=True)
    nationality = models.CharField(max_length=100, null=True)
    owner = models.ManyToManyField(Car, through='Ownership')

    def __str__(self):
        return f"CarOwner(first_name={self.first_name}, last_name={self.last_name}, birth_date={self.birth_date}, " \
               f"passport={self.passport}, home_Address={self.home_Address}, nationality={self.nationality})"


class Ownership(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    owner = models.ForeignKey(CarOwner, on_delete=models.DO_NOTHING)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(null=True)

    def __str__(self):
        return f"Ownership(car={self.car}, owner={self.owner}, date_start={self.date_start}, date_end={self.date_end})"


class DriverLicense(models.Model):
    owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE)
    number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    issue_date = models.DateTimeField()

    def __str__(self):
        return f"DriverLicense(owner={self.owner}, number={self.number}, license_type={self.license_type}, issue_date={self.issue_date})"
