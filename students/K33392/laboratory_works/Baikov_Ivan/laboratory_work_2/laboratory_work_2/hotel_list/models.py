# models.py
from django.db import models
from django.contrib.auth.models import User

class Hotel(models.Model):
    name = models.CharField(max_length=200)
    owner = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()
    room_types = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.PositiveIntegerField()
    amenities = models.TextField()
    
    def __str__(self):
        return self.name

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    num_guests = models.PositiveIntegerField()
    additional_notes = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f'Reservation for {self.user.username} at {self.hotel.name}'

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    review_text = models.TextField()  # Add the review_text field
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 11)])
    additional_comments = models.TextField()  # Add the additional_comments field
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Review by {self.user.username} for {self.hotel.name}'

    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username