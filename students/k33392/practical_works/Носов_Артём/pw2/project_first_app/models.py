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

class ExampleModel(models.Model):
  
    # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
  
    # renames the instances of the model
    # with their title name
    def __str__(self):
        return self.title
    
class Publisher(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  birthdate = models.DateField()

  def __str__(self):
    return "{} {}".format(self.first_name, self.last_name)

from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    name = models.CharField(max_length=100, blank=True, null=True)

    
from django.conf import settings
from django.contrib.auth import get_user_model
class Book(models.Model):
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return "{}, {}".format(self.name, self.publisher)
  
from django.contrib.auth.models import AbstractUser



