from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . import models
from django import forms
# from .models import User
from .models import User, Racer


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "first_name","last_name"]

class RacerForm(forms.ModelForm):
    class Meta:
        model = Racer
        fields = ["team", "car", "description", "experience", "klass"]