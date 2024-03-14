from django import forms
from .models import Passenger, Reservation, Comment


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ["username", "password", "first_name", "last_name", "email", "passport"]


class LoginForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ["username", "password"]


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ["room", "date_start", "date_finish"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["rating", "text"]
