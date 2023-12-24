from django.db import models


class User(models.Model):
    email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    password = models.CharField(max_length=255, blank=False, null=False)

    #  userprofile
    #  apitoken_set


class UserProfile(models.Model):
    first_name = models.CharField(max_length=255, blank=False, null=False)
    last_name = models.CharField(max_length=255, blank=False, null=False)
    patronymic = models.CharField(max_length=255, blank=False, null=False)

    user = models.OneToOneField('User', on_delete=models.CASCADE)


class ApiToken(models.Model):
    token = models.CharField(max_length=255, blank=False, null=False, unique=True)

    user = models.ForeignKey('User', on_delete=models.CASCADE)
