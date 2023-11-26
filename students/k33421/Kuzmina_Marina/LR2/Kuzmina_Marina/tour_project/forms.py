from django import forms
from .models import Review
from .models import Reservation

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['text', 'rating']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['user', 'tour']
