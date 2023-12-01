from django import forms
from datetime import date
from django.contrib.auth.forms import UserCreationForm

from .models import Ticket, Traveler, Flight, Seat, Comment


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket

        fields = ['baggage']
        labels = {
            'baggage': 'Багаж',
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('rating', 'text')


class SignUpForm(UserCreationForm):

    class Meta:
        model = Traveler
        fields = ('username', 'first_name', 'last_name', 'birth_date', 'passport', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'