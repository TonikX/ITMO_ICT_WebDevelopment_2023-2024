from django import forms
from .models import Reservation, Tour, Review


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['tour']


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['title', 'description', 'period', 'payment_conditions', 'user']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['tour', 'text', 'rating']
