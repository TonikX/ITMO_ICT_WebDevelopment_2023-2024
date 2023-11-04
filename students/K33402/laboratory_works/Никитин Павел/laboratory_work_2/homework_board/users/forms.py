from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm

from main.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User