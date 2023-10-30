from django import forms
from .models import Passenger, Reservation, Comment, Seat
from django.db.models import Q


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ["username", "password", "email", "passport"]


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["seat"]

    def __init__(self, flight, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)
        reservations = Reservation.objects.filter(flight=flight)
        reservation_seats = map(lambda reservation: reservation.seat.id, reservations)
        all_seats = Seat.objects.filter(flight=flight)
        result_seats = all_seats.filter(~Q(id__in=reservation_seats))
        self.fields['seat'].queryset = result_seats


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["rating", "text"]
