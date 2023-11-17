from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Flight, FlightReview, Reservation


class CustomUserCreationForm(UserCreationForm):
    passport_number = forms.CharField(max_length=20, required=False)
    phone_number = forms.CharField(max_length=15, required=False)

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('passport_number', 'phone_number')


class ReservationForm(forms.Form):
    flight = forms.ModelChoiceField(queryset=Flight.objects.all())
    ticket_number = forms.CharField(max_length=20)


class FlightReviewForm(forms.ModelForm):
    rating = forms.FloatField(
        min_value=0,
        max_value=5,
        widget=forms.NumberInput(attrs={'type': 'number', 'step': '1'})
    )

    class Meta:
        model = FlightReview
        fields = ['text', 'rating']


class FlightSeatForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['seat_number']
