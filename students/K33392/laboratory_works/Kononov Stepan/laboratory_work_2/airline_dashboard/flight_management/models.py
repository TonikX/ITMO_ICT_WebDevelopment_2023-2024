from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string


class User(AbstractUser):
    passport_number = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    airline = models.CharField(max_length=100)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    gate_number = models.CharField(max_length=10)
    total_seats = models.PositiveIntegerField(default=100)
    booked_seats = models.PositiveIntegerField(default=0)

    def available_seats(self):
        return self.total_seats - self.booked_seats

    def release_seat(self):
        self.booked_seats -= 1
        self.save()
        self.booked_seats = max(0, self.booked_seats)
        self.save()

    def book_seat(self):
        if self.available_seats() > 0:
            self.booked_seats += 1
            self.save()
            return True
        return False

    def __str__(self):
        return f"Flight {self.flight_number} - {self.departure_city} to {self.arrival_city}"


class Passenger(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    reservations = models.ManyToManyField(Flight, through='Reservation')

    def __str__(self):
        return f"Passenger: {self.user.username}"


class Reservation(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=5, unique=True, editable=False)
    seat_number = models.PositiveIntegerField(blank=True)

    def save(self, *args, **kwargs):
        flight = self.flight
        flight.book_seat()
        if not self.seat_number:
            available_seats = flight.available_seats()
            if available_seats > 0:
                for i in range(1, flight.total_seats + 1):
                    if not Reservation.objects.filter(flight=flight, seat_number=i).exists():
                        self.seat_number = i
                        break
            else:
                raise Exception("No available seats on this flight.")
        super(Reservation, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.flight.release_seat()
        super(Reservation, self).delete(*args, **kwargs)

    def __str__(self):
        return f"Reservation for {self.passenger.user.username} on Flight {self.flight.flight_number}, Seat {self.seat_number}"


class FlightReview(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    date = models.DateField()
    text = models.TextField()
    rating = models.IntegerField()
    commentator = models.ForeignKey(Passenger, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review for Flight {self.flight.flight_number} by {self.commentator.user.username}"


@receiver(pre_save, sender=Reservation)
def generate_ticket_number(sender, instance, **kwargs):
    if not instance.ticket_number:
        unique_ticket_number = get_random_string(length=5, allowed_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
        instance.ticket_number = unique_ticket_number
