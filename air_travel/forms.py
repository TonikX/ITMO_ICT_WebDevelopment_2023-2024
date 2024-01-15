from django import forms
from django.contrib.auth.forms import UserCreationForm

from air_travel.models import CustomUser, Comments


class NewPassengerForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

class CommentFlightForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text', 'rate']