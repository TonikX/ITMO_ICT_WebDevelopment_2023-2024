from django import forms
from .models import TourComment, Reservation

class CommentForm(forms.ModelForm):
    class Meta:
        model = TourComment
        fields = ['text', 'rating']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['start_date', 'end_date']
        # fields = ['reservation_date', 'status']
