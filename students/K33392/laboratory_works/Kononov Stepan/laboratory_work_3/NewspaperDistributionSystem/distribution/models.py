from django.contrib.auth.models import AbstractUser
from django.db import models


class Editor(AbstractUser):
    middle_name = models.CharField(max_length=255)
    REQUIRED_FIELDS = ['email', 'middle_name']

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}"


class PrintingHouse(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=[('открыта', 'Открыта'), ('закрыта', 'Закрыта')])

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    name = models.CharField(max_length=255)
    edition_index = models.CharField(max_length=255)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    price_per_copy = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class PrintRun(models.Model):
    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE)
    printing_house = models.ForeignKey(PrintingHouse, on_delete=models.CASCADE)
    copies_count = models.IntegerField()

    def __str__(self):
        return f"{self.newspaper.name} ({self.copies_count} copies) - {self.printing_house.name}"


class PostOffice(models.Model):
    number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.number


class PostalArrival(models.Model):
    post_office = models.ForeignKey(PostOffice, on_delete=models.CASCADE)
    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE)
    copies_received = models.IntegerField()

    def __str__(self):
        return f"{self.newspaper.name} ({self.copies_received} copies) - {self.post_office.number}"
