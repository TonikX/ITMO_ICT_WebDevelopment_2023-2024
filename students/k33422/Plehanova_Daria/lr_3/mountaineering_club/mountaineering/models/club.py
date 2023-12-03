from django.db import models


class Club(models.Model):
	name = models.CharField(max_length=100)
	country = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	contact_person = models.CharField(max_length=100)
	email = models.EmailField()
	phone = models.CharField(max_length=20)
	website = models.URLField(blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.name
