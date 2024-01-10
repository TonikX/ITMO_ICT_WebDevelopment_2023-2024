from django.contrib.auth import get_user_model
from django.db import models

from .club import Club

User = get_user_model()


class Alpinist(models.Model):
	LEVEL_CHOICES = [
		('Beginner', 'Beginner'),
		('Intermediate', 'Intermediate'),
		('Advanced', 'Advanced'),
		('Expert', 'Expert'),
	]
	
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='alpinist_profile')
	date_of_birth = models.DateField()
	address = models.TextField()
	level = models.CharField(max_length=20, choices=LEVEL_CHOICES, default='Beginner')
	club = models.ForeignKey(Club, on_delete=models.SET_NULL, null=True, blank=True, related_name='alpinists')
	
	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name}"
