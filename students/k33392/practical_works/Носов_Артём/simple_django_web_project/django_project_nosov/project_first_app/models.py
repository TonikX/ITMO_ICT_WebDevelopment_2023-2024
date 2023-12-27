from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Dog(models.Model):
    owner_dog = models.ForeignKey(Owner,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    class_dog = models.CharField(max_length=30)

class Exhibition(models.Model):
    TYPE_EX = (
    ('C1', 'CACIB'),
    ('C2', 'CAC'),
    ('M', 'MONO'),
    )
    name_ex = models.CharField(max_length=100)
    date_b = models.DateField()
    date_c = models.DateField()
    type = models.CharField(max_length=2, choices=TYPE_EX)
    member = models.ManyToManyField(Dog, through='Participate')

class Participate(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    date_reg = models.DateField()