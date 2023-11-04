from django.db import models


class Car(models.Model):
    state_number = models.CharField(max_length=15, null=False)
    brand = models.CharField(max_length=20, null=False)
    model = models.CharField(max_length=20, null=False)
    color = models.CharField(max_length=30, null=True)
    owners = models.ManyToManyField('CarOwner', through='CarOwn')

    def __str__(self):
        return f"{self.state_number} {self.brand} {self.model}"


class CarOwner(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    second_name = models.CharField(max_length=30, null=False)
    birthday = models.DateField(null=True)
    cars = models.ManyToManyField('Car', through='CarOwn')

    def __str__(self):
        return f"{self.first_name} {self.second_name}"


class DriverLicense(models.Model):
    owner_id = models.ForeignKey(CarOwner, on_delete=models.PROTECT, null=False)
    license_number = models.CharField(max_length=10, null=False)
    license_type = models.CharField(max_length=10, null=False)
    issue_date = models.DateField(null=False)

    def __str__(self):
        return f"{self.license_number} {self.owner_id.first_name} {self.owner_id.second_name}"


class CarOwn(models.Model):
    car_owner = models.ForeignKey(CarOwner, on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.car.state_number} {self.car_owner.first_name}  {self.car_owner.second_name}"