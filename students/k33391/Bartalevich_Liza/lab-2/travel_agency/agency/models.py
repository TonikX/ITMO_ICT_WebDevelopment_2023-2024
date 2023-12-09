from django.db import models
from django.contrib.auth.models import User


class Agency(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)

    def str(self):
        return self.name


class Tour(models.Model):
    name = models.CharField(max_length=200)
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name='tours')
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    country = models.CharField(max_length=200)
    payment_conditions = models.TextField()

    def str(self):
        return self.name


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reservations')
    reserved_on = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    def str(self):
        return f"{self.user.username} - {self.tour.name}"


class Review(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    comment_date = models.DateField(auto_now_add=True)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 11)])

    def str(self):
        return f"{self.user.username} - {self.rating}/10"
