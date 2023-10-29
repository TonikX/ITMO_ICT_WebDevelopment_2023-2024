# Импортируем необходимые модули
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.conf import settings



# Создаем модель CustomUser, которая будет расширять стандартную модель User
class CustomUser(AbstractUser):
    passport_number = models.CharField(max_length=20, blank=True, null=True)  # Поле для номера паспорта
    home_address = models.CharField(max_length=255, blank=True, null=True, default="Default Address")  # Поле для домашнего адреса
    nationality = models.CharField(max_length=50, blank=True, null=True)  # Поле для национальности

    # Функция, которая возвращает строковое представление пользователя
    def __str__(self):
        return self.username



# Модель OwnerProfile, для связи с пользователем
class OwnerProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    passport_number = models.CharField(max_length=20)
    home_address = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username







# Модель автомобилей
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    license_plate = models.CharField(max_length=15)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)

# Модель владельцев автомобилей
class Owner(models.Model):
    owner_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateTimeField(null=True)



# Модель владения автомобилем
class Ownership(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(null=True)

# Модель водительских удостоверений
class DriverLicense(models.Model):
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    license_type = models.CharField(max_length=10)
    issue_date = models.DateTimeField()


class ExampleModel(models.Model):
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title