from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm
from .models import Booking, Review


class GuestCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2',
                  'email', 'first_name', 'last_name',
                  'country', 'photo']


class BookingCreationForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['guest', 'room', 'date_from',
                  'date_until', 'status']


class ReviewCreationForm(ModelForm):
    class Meta:
        model = Review
        fields = ['booking', 'rating', 'body']
