from django import forms
from .models import Booking, Feedback, Guest


class BookingForm(forms.Form):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    passport = forms.CharField()
    check_in_date = forms.DateField()
    check_out_date = forms.DateField()


class FeedbackForm(forms.Form):
    text = forms.CharField(max_length=20)
    rate = forms.IntegerField()
