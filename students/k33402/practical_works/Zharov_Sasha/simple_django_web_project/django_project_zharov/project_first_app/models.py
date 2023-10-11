from django.db import models


class Driver(models.Model):
    first_name = models.CharField('Имя', max_length=30)
    last_name = models.CharField('Фамилия', max_length=30)
    birth_date = models.DateTimeField('Дата рождения', null=True)  # needed that for creating a superuser
    cars = models.ManyToManyField('Car', through='Ownership')

    def __str__(self):
        return self.first_name, self.last_name


class Ownership(models.Model):
    car = models.ForeignKey('Car', null=True, on_delete=models.CASCADE)
    driver = models.ForeignKey('Driver', null=True, on_delete=models.CASCADE)
    date_start = models.DateField('Дата начала')
    date_end = models.DateField('Дата окончания')


class Car(models.Model):
    number = models.CharField('Гос номер', max_length=15)
    brand = models.CharField('Марка', max_length=20)
    car_model = models.CharField('Модель', max_length=20)
    color = models.CharField('Цвет', max_length=30, blank=True, null=True)
    drivers = models.ManyToManyField('Driver', through='Ownership')

    def __str__(self):
        return self.number, self.car_model


class DriverLicence(models.Model):
    owner = models.ForeignKey('Driver', on_delete=models.CASCADE)
    number = models.CharField('Номер удостоверения', max_length=10)
    type = models.CharField('Тип', max_length=10)
    release_date = models.DateTimeField('Дата выдачи')











