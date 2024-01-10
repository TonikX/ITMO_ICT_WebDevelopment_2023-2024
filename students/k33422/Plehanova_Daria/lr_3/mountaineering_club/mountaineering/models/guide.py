from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Guide(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='guide_profile')
	certification = models.CharField(max_length=100)
	years_of_experience = models.PositiveIntegerField()
	
	def __str__(self):
		return f"{self.user.first_name} {self.user.last_name}"
