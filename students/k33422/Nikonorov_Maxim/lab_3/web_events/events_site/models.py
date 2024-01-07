from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from rest_framework.authtoken.models import Token


class EventsUser(AbstractUser):
    LastName = models.CharField(null=False, max_length=30)
    FirstName = models.CharField(null=False, max_length=30)
    DateOfBirth = models.DateField(null=True, blank=True)
    PhoneNumber = models.CharField(null=True, max_length=30, blank=True)
    IsSubscribed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if not Token.objects.filter(user=self).exists():
            Token.objects.create(user=self)
            
    def __str__(self):
        return f"user {self.LastName} {self.FirstName}"

class EventCard(models.Model):
    PostTitle = models.CharField(null=False, max_length=70)
    EventType = models.ForeignKey('EventTypeList', null=False, on_delete=models.CASCADE)
    Description = RichTextField(null=False)
    DateOfEvent = models.DateField(null=False, default=timezone.now)
    EventPlace = models.ForeignKey('Place', null=False, on_delete=models.CASCADE)
    NumberOfParticipants = models.PositiveIntegerField(null=False) 
    restictions = (
        ('18', '18+'),
        ('16', '16+'),
        ('12', '12+'),
        ('0', 'no age restriction'),
    )
    AgeRestriction = models.CharField(max_length=20, choices=restictions)
    statuses = (
        ('OPENED', 'opened'),
        ('CANCELED', 'canceled'),
        ('CLOSED', 'closed'),
    )
    Status = models.CharField(max_length=20, choices=statuses)
    
    def __str__(self):
        return self.PostTitle
    
    def clean(self):
        if self.NumberOfParticipants > self.EventPlace.PlaceCapacity:
            raise ValidationError("Number of participants can't exceed place capacity.")
        
        if self.DateOfEvent < timezone.now().date():
            raise ValidationError("Event date cannot be earlier than today.")

class EventTypeList(models.Model):
    TypeTitle = models.CharField(null=False, max_length=20)
    Description = models.CharField(null=False, max_length=150)
    Colour = models.CharField(null=False, max_length=7)
    
    def __str__(self):
        return self.TypeTitle
    
class Place(models.Model):
    PlaceTitle = models.CharField(null=False, max_length=30)
    PlaceAddress = models.CharField(null=False, max_length=70)
    PlaceCapacity = models.PositiveIntegerField(null=False)
    
    def __str__(self):
        return self.PlaceTitle
    
class UsersEventsList(models.Model):
    EventUser = models.ForeignKey('EventsUser', null=False, on_delete=models.CASCADE)
    EventCard = models.ForeignKey('EventCard', null=False, on_delete=models.CASCADE, related_name='events_users_list')
    TimeOfRegistration = models.DateField(null=False, default=timezone.now)
    
    class Meta:
        unique_together = ('EventUser', 'EventCard')
        
    def __str__(self):
        return f"{self.EventUser} {self.EventCard}"
    
    def clean(self):
        if self.EventCard.NumberOfParticipants <= self.EventCard.events_users_list.count():
            raise ValidationError("Registration is closed due to lack of available places")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
class SubscribedEmail(models.Model):
    User = models.OneToOneField('EventsUser', on_delete=models.CASCADE)
    Email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.Email

