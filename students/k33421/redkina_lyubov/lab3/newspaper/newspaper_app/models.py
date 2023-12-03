from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_postoffice_number = models.CharField(max_length=50)


class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    edition_index = models.CharField(max_length=50)
    editor_last_name = models.CharField(max_length=255)
    editor_first_name = models.CharField(max_length=255)
    editor_middle_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)


class PrintingHouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    is_closed = models.BooleanField(default=False)


class PostOffice(models.Model):
    number = models.IntegerField()
    address = models.TextField()


class NewspaperPrint(models.Model):
    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE)
    printing_house = models.ForeignKey(PrintingHouse, on_delete=models.CASCADE)
    circulation = models.IntegerField()


class NewspaperArrival(models.Model):
    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE)
    post_office = models.ForeignKey(PostOffice, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class NewspaperOrder(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
