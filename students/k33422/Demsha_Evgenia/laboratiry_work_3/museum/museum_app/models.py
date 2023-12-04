from django.db import models
from django.contrib.auth.models import User


class Museum(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    director = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    country = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name}'


class Set(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Item(models.Model):
    name = models.CharField(max_length=50)
    inventory_number = models.IntegerField()
    set = models.ForeignKey(Set, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    creation_date = models.DateField()
    is_date_exact = models.BooleanField(default=False)
    country = models.CharField(max_length=30, null=True, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return f'{self.name}'


class Foundation(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE)
    curator = models.ForeignKey(User, on_delete=models.CASCADE)
    set = models.ManyToManyField(Set, through='SetToFoundation')

    def __str__(self):
        return f'{self.name}'


class Exhibition(models.Model):
    name = models.CharField(max_length=50)
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE)
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=12)
    open_date = models.DateField()
    close_date = models.DateField()

    item = models.ManyToManyField(Item, through='ItemToExhibition')

    def __str__(self):
        return self.name


class ItemToExhibition(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)
    send_date = models.DateField()
    return_date = models.DateField()
    director_signature = models.BooleanField(default=False)
    curator_signature = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.item} оn {self.exhibition}'


class SetToFoundation(models.Model):
    set = models.ForeignKey(Set, on_delete=models.CASCADE)
    foundation = models.ForeignKey(Foundation, on_delete=models.CASCADE)
    send_date = models.DateField()
    return_date = models.DateField()
    director_signature = models.BooleanField(default=False)
    curator_signature = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.set} in {self.foundation}'

