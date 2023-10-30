from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Agency(models.Model):
    name = models.CharField(max_length=255)
    #description = models.CharField(max_length=255)

class Tour(models.Model):
    name = models.CharField(max_length=255)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    payment_conditions = models.TextField()


class Users(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')



class Reservation(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)

class Review(models.Model):
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)