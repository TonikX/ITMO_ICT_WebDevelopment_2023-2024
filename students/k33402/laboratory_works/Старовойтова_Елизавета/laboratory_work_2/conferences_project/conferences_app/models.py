from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    surname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    passport = models.CharField(max_length=20)

class Conference(models.Model):
    members = models.ManyToManyField(User, through='AuthorRegistration', related_name='conferences_attending')
    name = models.CharField(max_length=100)
    date = models.DateField()
    topics = models.TextField()
    location = models.CharField(max_length=100)


class AuthorRegistration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    date_registered = models.DateTimeField(auto_now=True)
    presentation_title = models.CharField(max_length=255)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, related_name='comments')
    date_created = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    rating = models.IntegerField()

