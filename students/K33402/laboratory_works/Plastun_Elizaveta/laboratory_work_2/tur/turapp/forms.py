from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name", "email"]


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User


class CommentForm(forms.ModelForm):
    class Meta:
        model = TourComment
        fields = ['text', 'rating']


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['start_date', 'end_date']


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = ['name', 'agency_name', 'country', 'description', 'start_date', 'end_date', 'price', ]
