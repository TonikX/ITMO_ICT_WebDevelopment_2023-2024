from django.utils import timezone

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

from django.conf import settings
# Create your models here.


class Person(AbstractUser):
    email = models.EmailField(default="example@notset.com")
    #accountCreationDate = models.DateField(blank=True, default=timezone.now())
    lastUpdate = models.DateField(blank=True, default=timezone.now())
    capCount = models.IntegerField(blank=True, default=0)
    friends = models.ManyToManyField(
        "self",
        symmetrical=False,
        through="FriendShip",
    )
    birthDate = models.DateField(null=True, blank=True)
    #fullName = models.CharField(null=True, blank=True, default="Nemo", max_length=100)
    last_login = models.DateField(blank=True, default=timezone.now())

class FriendShip(models.Model):
    fromPersonID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    toPersonID = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="toPerson")
    statusVariation = [
        ("aw", "awaiting confirmation"),
        ("a", "approved"),
        ("r", "rejected"),
    ]
    sendDate = models.DateField(blank=True, default=timezone.now())
    approvedDate = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=6, choices=statusVariation, default='aw')


class Vault(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    cDate = models.DateTimeField(blank=True, default=timezone.now())
    eDate = models.DateTimeField()
    accessVariation = [
        ("ffa", "Everybody can open capsule and leave comment"),
        ("my", "Only for me"),
        ("ff", "For me and my friends. Friends can open and leave comment"),
        ("custom", "Custom access list"),
    ]
    access = models.CharField(max_length=6, choices=accessVariation, default='my')
    customAccessList = models.ManyToManyField(settings.AUTH_USER_MODEL, through='VaultAccess')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="owner_set")

    text = models.TextField(null=True, blank=True)


class File(models.Model):
    vault = models.ForeignKey(Vault, on_delete=models.CASCADE)
    filename = models.CharField(max_length=100)
    extension = models.CharField(max_length=20)
    path = models.CharField(max_length=4000)


class VaultAccess(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vault = models.ForeignKey(Vault, on_delete=models.CASCADE)
    accessVariation = [
        ("see", "Only can see the preview"),
        ("open", "Can open capsule"),
        ("r&c", "Can open capsule and comment"),
    ]
    permissions = models.CharField(max_length=6, choices=accessVariation, default='os')


class Comments(models.Model):
    person = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vault = models.ForeignKey(Vault, on_delete=models.CASCADE, default=1)
    commentText = models.TextField()
    commentDate = models.DateTimeField(blank=True, default=timezone.now())
    mainComment = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="set_main_comment")
    subComments = models.ManyToManyField("self", blank=True, symmetrical=False)



