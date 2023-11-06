# forms.py в вашем приложении hotels
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Visitor, Reservation, Review


class VisitorCreationForm(UserCreationForm):
    class Meta:
        model = Visitor
        fields = ('username', 'email', 'surname', 'name', 'passport',
                  'password1', 'password2')


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['room_type', 'start_date', 'end_date']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'stay_from', 'stay_to', 'comment', 'author']
        widgets = {
            'stay_from': forms.DateInput(attrs={'type': 'date'}),
            'stay_to': forms.DateInput(attrs={'type': 'date'}),
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 10})
        }