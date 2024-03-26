from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=200, null=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    date_registered = models.DateTimeField(auto_now_add=True, null=True)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Conference(models.Model):
    name = models.CharField(max_length=200)
    user_registered = models.ManyToManyField(User, null=True, blank=True)
    location = models.CharField(max_length=200)
    date = models.DateTimeField(null=True)
    description = models.TextField(null=True)
    location_description = models.TextField(null=True)
    participating_terms = models.TextField(null=True)

    def __str__(self):
        return self.name


class Performance(models.Model):
    conference = models.ForeignKey(Conference, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.CharField(max_length=200, null=True)
    result = models.BooleanField(null=True)

    def __str__(self):
        return self.topic


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    text = models.TextField(null=True)
    conference = models.ForeignKey(Conference, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(null=True)

    def __str__(self):
        return self.text
