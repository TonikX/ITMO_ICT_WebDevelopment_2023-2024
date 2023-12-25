from django.db import models
from django.contrib.auth.models import User


class Museum(models.Model):
    name = models.CharField(max_length=100)
    director = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=150)
    inventory_number = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True, related_name='work')
    image = models.ImageField(null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    creation_year = models.IntegerField()
    is_year_exact = models.BooleanField(default=False)
    description = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=150)
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='item')
    number = models.IntegerField()
    description = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Foundation(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE, related_name='foundation')
    curator = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ManyToManyField(Card, through='CardToFoundation', related_name='foundation')

    def __str__(self):
        return self.name


class Exhibition(models.Model):
    name = models.CharField(max_length=50)
    museum = models.ForeignKey(Museum, on_delete=models.CASCADE, related_name='exhibition')
    description = models.CharField(max_length=1000)
    address = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=50)
    contact_phone = models.CharField(max_length=12)
    open_date = models.DateField()
    close_date = models.DateField()
    item = models.ManyToManyField(Item, through='ItemToExhibition', related_name='exhibition')

    def __str__(self):
        return self.name


class ItemToExhibition(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='sending_to_exhibition')
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE, related_name='item_sending')
    send_date = models.DateField()
    return_date = models.DateField()
    director_signature = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.item} оn {self.exhibition}'


class CardToFoundation(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='sending_to_foundation')
    foundation = models.ForeignKey(Foundation, on_delete=models.CASCADE, related_name='card_sending')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    director_signature = models.BooleanField(default=False)
    curator_signature = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.card} in {self.foundation}'

#
# python3 manage.py graph_models -a -I User,Museum,Author,Card,Item,Foundation,Exhibition,ItemToExhibition,CardToFoundation -o myapp_models.png
