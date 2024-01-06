from django import forms

from .models import Reservation, Review


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['registered', 'seat']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']
