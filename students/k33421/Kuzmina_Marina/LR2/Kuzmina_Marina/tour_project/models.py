from django.db import models
from django.contrib.auth.models import User

class Tour(models.Model):
    title = models.CharField(max_length=100)
    agency = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    payment_conditions = models.TextField()
    is_sold = models.BooleanField(default=False)

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)

class Review(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.tour.name} by {self.user.username}"

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


